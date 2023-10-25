from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('importCSV')
  #  anvil.server.call('runBackground')  
  #anvil.server.call('runTask')
    #anvil.server.launch_background_task("runTask")

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('countRows')

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("download_file")

  def outlined_button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("hello")




