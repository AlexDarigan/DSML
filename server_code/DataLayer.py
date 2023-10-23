import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from pandas import pandas as pd

# This is used to access our prefiltered data
@anvil.server.callable
def get_color_distribution():
  cards = app_tables.cards.search()
  red = len(app_tables.cards.search(colors=["R"]))
  blue = len(app_tables.cards.search(colors=["U"]))
  green = len(app_tables.cards.search(colors=["G"]))
  black = len(app_tables.cards.search(colors=["B"]))
  white = len(app_tables.cards.search(colors=["W"]))
  colorless = len(app_tables.cards.search(colors=[]))
  return (["Red", "Blue", "Black", "Green", "White", "Colorless"], [red, blue, green, black, white, colorless])

@anvil.server.callable
def do_pandas():
  df = pd.DataFrame(app_tables.cards.search())
  print(df.head())