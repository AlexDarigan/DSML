import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
from pandas import pandas as pd

# This is used to access our prefiltered data
@anvil.server.callable
def get_color_distribution():
  df = pd.read_csv(data_files['cards.csv'], keep_default_na=False, encoding = "utf-8")


  blue = len(df[df.blue])
  red = len(df[df.red])
  #blue = len(df[df.blue])
  green = len(df[df.green])
  #black = df["black"].sum()
  black = 10
  white = len(df[df.white])
  colorless = len(df[df.colorless])
  return (["Red", "Blue", "Black", "Green", "White", "Colorless"], [red, blue, green, black, white, colorless])
