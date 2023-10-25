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

    color, color_count = anvil.server.call('get_color_distribution')
    year, year_count = anvil.server.call('get_cards_released_per_year')


    self.colors_plot.layout = {
       "title": "Count of cards released by year",
    }
    
    self.colors_plot.data = [
      go.Pie(
        labels=color,
        values=color_count
      )
    ]


    self.release_plot.layout = {
      "title": "Count of cards released by year",
      "xaxis": {
        "title": 'Count'
      },
      "yaxis": {
        "title": "Year",
        "dtick": 1,
        "tickmode": "linear",
        "spacing": 10,
      }
    }
    self.release_plot.data = [
        go.Bar(
          dy=1,
          x = year_count,
          y = year,
          orientation="h",
          name = "Cards released by year",
        ),
    ]





