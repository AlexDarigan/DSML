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
  task = anvil.server.launch_background_task('getData')
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
def getData():
  response = requests.get("https://api.scryfall.com/bulk-data/default-cards") # The download uri this points to is a json file with over 400,000 files.
  if response.status_code != 200:
    print("Response failed with status code: " + str(response.status_code))
  data = response.json()
  if data:
    print(data)
  download = data["download_uri"]
  downloaded = requests.get(download) #, stream=True)
  # downloaded = anvil.http.request(download)  # An API that provides slow responses
  if downloaded.status_code != 200:
    print("err")
  lines = []
  line_num = 0
  for line in downloaded.iter_lines():
    if len(line) == 1:
      continue
    #data.append(json.loads(line.decode("utf-8")[:-1]))
    #lines.append(line.decode("utf-8")[:-1])

    print(line.decode("utf-8")[:-1])
    line_num += 1
    # if line_num > 1000:
    #   break
  print(line_num)
  print("got cards")
  
    
  return "Hello World"

  
