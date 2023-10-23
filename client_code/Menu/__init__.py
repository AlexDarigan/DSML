from ._anvil_designer import MenuTemplate
from anvil import *
import anvil.server

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def about_me_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Bio')

  def projects_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DSML')



