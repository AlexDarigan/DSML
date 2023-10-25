from ._anvil_designer import DSMLTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import anvil.server

class DSML(DSMLTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    labels, values = anvil.server.call('get_color_distribution')
    print(labels)
    print(values)
    self.colors_plot.data = [
      go.Pie(
        labels=labels,
        values=values
      )
    ]






