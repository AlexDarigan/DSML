import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from pandas import pandas
import requests

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

@anvil.server.callable
def download_file():
  # GET BULK DATA
  response = requests.get("https://api.scryfall.com/bulk-data/default-cards")
  if response.status_code != 200:
    print("Response failed with status code " + str(response.status_code))
  data = response.json()

  # DOWNLOAD CARD DATA
  download = data["download_uri"]
  print("downloading")
  downloaded = requests.get(download) # stream=True)
  if downloaded.status_code != 200:
    print("Download failed with status code: " + str(downloaded.status_code))

  print("downloaded")
 # print(downloaded.content.decode("utf-8"))
 # df = pandas.DataFrame(downloaded.content)
 # print(len(df))
  print("begin")
  data = ""
  count = 0
  for row in downloaded.iter_lines():
    count += 1
    print(count)
    data += row.decode("utf-8")
  file = File(data=data, name="cardstest.json")
  app_tables.files.add_row(file=file)
  print("done")
#   # count = 0
#   # for row in downloaded.iter_lines():
#   #   print(row.decode("utf-8"))
#   #   count += 1
#   # print("count ", count)
#   data = "This is the content you want to save as a file."

# # Create a new file in the File Store
# file = File(data=data, name="example.txt")

# # Save the file to the File Store
# app_tables.file_store.add_row(file=file)