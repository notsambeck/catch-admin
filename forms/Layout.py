from anvil import *
import anvil.server
import anvil.users
import tables
from tables import app_tables
from Users import Users

class Layout(LayoutTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    self.content_panel.add_component(Users())


  def user_button_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Users())

    # Any code you write here will run when the form opens.
    
