from ._anvil_designer import DSMLTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class DSML(DSMLTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def color_distribute_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    labels, values = anvil.server.call('get_color_distribution')
    self.colors_plot.data = [
      go.Pie(
        labels=labels,
        values=values
      )
    ]

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('do_pandas')

  

