from ._anvil_designer import DSMLTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class DSML(DSMLTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.api_design.content = self.api_design.content.replace("api.hostname", anvil.server.get_api_origin())
    
    color = ["red", "green", "blue", "black", "white", "colorless"]
    color_count = [15541, 16051, 15404, 15714, 15972, 19146]
    
    self.colors_plot.layout = {
       "title": "Color Distribution",
    }
    
    self.colors_plot.data = [
      go.Pie(
        labels=color,
        values=color_count
      )
    ]

    year = [*range(1993, 2023)]
    year_count = [1596, 1643, 1728, 1020, 1607, 1162, 1639, 913, 1584, 823, 1610, 946, 
                  2120, 1107, 1494, 1310, 1538, 1787, 2085, 1461, 2080, 2806, 2747, 
                  2841, 3427, 3746, 4754, 6557, 6972, 11564, 8788, 124]
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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_1.visible = not self.image_1.visible






