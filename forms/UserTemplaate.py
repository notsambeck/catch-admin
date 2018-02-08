from anvil import *
import anvil.server
import anvil.users
import tables
from tables import app_tables

class UserTemplaate (UserTemplaateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

  def button_1_click (self, **event_args):
    # This method is called when the button is clicked
    count = self.parent.parent.action_data.search(user=self.item)
    self.label_2.text = count
    # Any code you write here will run when the form opens.