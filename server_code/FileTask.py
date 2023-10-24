import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from pandas import pandas

@anvil.server.callable
def importCSV():  
  task = anvil.server.launch_background_task('background_importCSV')
  if task.is_completed():
    print(task.get_return_value())

@anvil.server.background_task
@tables.in_transaction
def background_importCSV():
  count = 0
  df = pandas.read_csv(data_files['cards.csv'], keep_default_na=False, encoding = "utf-8")
  for d in df.to_dict(orient="records"):
      app_tables.cards.add_row(**d)
      count += 1
      print(count)
  return count
  