from anvil import *
import anvil.server
import anvil.users
import tables
from tables import app_tables

class Users (UsersTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    self.user_data = app_tables.catch_users.client_readable()
    self.action_data = app_tables.user_actions.client_readable()
    self.repeating_panel_1.items = self.user_data.search()
    # Any code you write here will run when the form opens.