from anvil import *
import anvil.server
import anvil.users
import tables
from tables import app_tables

class Users (UsersTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.test_on = False
    self.init_components(**properties)
    self.users = app_tables.catch_users.client_readable()
    self.actions = app_tables.user_actions.client_readable()
    
  def button_1_click (self, **event_args):
    # This method is called when the button is clicked
    self.test_on = not self.test_on
    self.repeating_panel_1_show()

  def repeating_panel_1_show (self, **event_args):
    # This method is called when the Label is shown on the screen
    if self.test_on:
      self.repeating_panel_1.items = self.users.search()
    else:
      self.repeating_panel_1.items = self.users.search(user_type='')
