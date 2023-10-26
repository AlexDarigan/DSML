from ._anvil_designer import MenuTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Menu(MenuTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def about_me_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Bio')

  def projects_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DSML')

  def restapi_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('REST')




