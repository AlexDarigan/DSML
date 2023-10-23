import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import pandas
import json
import timeit
import requests
import sys
import anvil.http
from io import BytesIO


@anvil.server.callable()
def runBackground():
  task = anvil.server.launch_background_task('getBulkCardData')
  if task.is_completed():
    print("completed")
    print(task.get_return_value())

   # If the task raised an exception, re-raise it here
  task.get_error()

  # # Otherwise, kill the task
  # task.kill()

  # # Check the termination status
  # if task.get_termination_status() == "killed":
  #   print("Yes, the task was killed!")
  #   print(task.get_return_value())

  # Finally, return the task to the client
  return task
    
@anvil.server.background_task
def getBulkCardData():
    # Requesting link for bulk English card data
    response = requests.get("https://api.scryfall.com/bulk-data/default-cards") # The download uri this points to is a json file with over 400,000 files.
    if response.status_code != 200:
        print("Response failed with status code: " + str(response.status_code))
        return response.status_code
    download_link = response.json()["download_uri"]
    downloaded = requests.get(download_link, stream=True)
    if downloaded.status_code != 200:
        return response.status_code
    
    # Processing Card Records
    records = 0
    for line in downloaded.iter_lines():
        # Skipping '[' & ']'
        if len(line) == 1:
            continue
        card = json.loads(line.decode("UTF8").rstrip(','))
        if card_row_exists(card["id"]):
          update_row(card)
        else:
          records += add_card(card)
    print(f'processed {records} new records')
    return records

def card_row_exists(cardId):
  return len(app_tables.cards.search(id=cardId)) > 0
  
# Double Check CMC, TypeLine & Oracle Text
# Some cards are double-sided, so right now we're just going to skip any cards with "transform keyword"
def add_card(card):
  if "card_faces" in card:
    # Skipping double-faced cards for now
    return 0
  print(card["name"])
  app_tables.cards.add_row(id=card["id"],
                          name=card["name"],
                          released_at=card["released_at"],
                          uri=card["uri"],
                          mana_cost=card["mana_cost"],
                          cmc=int(card["cmc"]),
                          type_line=card["type_line"],
                          oracle_text=card.get("oracle_text"),
                          power= card.get("power", "N/A"),
                          toughness= card.get("toughness", "N/A"),
                          colors=card["colors"],
                          keywords=card["keywords"],         
                          legalities={
                            "standard": card["legalities"]["standard"],
                            "modern": card["legalities"]["modern"],
                            "legacy": card["legalities"]["legacy"],
                            "vintage": card["legalities"]["vintage"]
                          },
                          reserved=card["reserved"],
                          foil=card["foil"],
                          nonfoil=card["nonfoil"],
                          finishes=card["finishes"],
                          promo=card["promo"],
                          reprint=card["reprint"],
                          variation=card["variation"],
                          set_id = card["set_id"],
                          rarity = card["rarity"],
                          full_art = card["full_art"],
                          usd = to_float(card["prices"]["usd"]),
                          usd_foil = to_float(card["prices"]["usd_foil"]),
                          eur = to_float(card["prices"]["eur"]),
                          eur_foil = to_float(card["prices"]["eur_foil"]))
  return 1

def update_row(card):
  row = app_tables.cards.search(id=card["id"])[0]
  row["usd"] = to_float(card["prices"]["usd"])
  row["usd_foil"] = to_float(card["prices"]["usd_foil"])
  row["eur"] = to_float(card["prices"]["eur"])
  row["eur_foil"] = to_float(card["prices"]["eur_foil"])

def to_float(source):
  if source is None:
    return 0.0
  return float(source)
  
