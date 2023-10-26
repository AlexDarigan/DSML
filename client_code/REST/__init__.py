from ._anvil_designer import RESTTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class REST(RESTTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.details.content = self.details.content.replace("api.hostname", anvil.server.get_api_origin())

    # Any code you write here will run before the form opens.
