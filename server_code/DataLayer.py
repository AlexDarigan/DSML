import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
from pandas import pandas as pd
import anvil.tables.query as q
import timeit

# This is used to access our prefiltered data
@anvil.server.callable
def get_color_distribution():
  timer = timeit.timeit()
  blue = len(app_tables.cards.search(blue=True))
  red = len(app_tables.cards.search(red=True))
  green = len(app_tables.cards.search(green=True))
  black = len(app_tables.cards.search(black=True))
  white = len(app_tables.cards.search(white=True))
  colorless = len(app_tables.cards.search(colorless=True))
  print(timer)
  return (["Red", "Blue", "Black", "Green", "White", "Colorless"], [red, blue, green, black, white, colorless])
