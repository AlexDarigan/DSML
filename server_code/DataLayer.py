import anvil.server
import anvil.tables.query as q
from anvil.tables import app_tables
import timeit

# This is used to access our prefiltered data
@anvil.server.callable
def get_color_distribution():
  timer = timeit.timeit()
  app_tables.cards.search(black="Tryu")
  blue = len(app_tables.cards.search(blue=True))
  red = 0 #len(app_tables.cards.search(red=True))
  green = len(app_tables.cards.search(green=True))
  black = len(app_tables.cards.search(black=True))
  white = len(app_tables.cards.search(white=True))
  colorless = len(app_tables.cards.search(colorless=True))
  print(blue, black, red, green, white, colorless)
  return (["Red", "Blue", "Black", "Green", "White", "Colorless"], [red, blue, green, black, white, colorless])
