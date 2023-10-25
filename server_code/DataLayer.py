import anvil.server
import anvil.tables.query as q
from anvil.tables import app_tables
import timeit
from datetime import datetime
import pandas as pd

# This is used to access our prefiltered data
@anvil.server.callable
def get_color_distribution():
  timer = timeit.timeit()
  print(app_tables.cards.search().to_csv().get_url())
  df = pd.read_csv(app_tables.cards.search().to_csv())
  blue = 0 # len(app_tables.cards.search(blue=True).to_csv())
  red = 0 #len(app_tables.cards.search(red=True).to_csv())
  green = 0 # len(app_tables.cards.search(green=True).to_csv())
  black = 0 #len(app_tables.cards.search(black=True).to_csv())
  white = 0 #len(app_tables.cards.search(white=True).to_csv())
  colorless = 0 # len(app_tables.cards.search(colorless=True).to_csv())
  return (["Red", "Blue", "Black", "Green", "White", "Colorless"], [red, blue, green, black, white, colorless])

@anvil.server.callable
def get_cards_released_per_year():
  count = []
  years = [*range(1993, 2024, 1)]
  for year in years:
    cards = app_tables.cards.search(released_at=q.between(datetime(day=1, month=1, year=year), datetime(day = 31, month = 12, year=year), max_inclusive=True))
    count.append(len(cards))
  return years, count
