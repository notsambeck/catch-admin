from anvil import *
import anvil.server
import anvil.users
import tables
from tables import app_tables

class UserTemplaate (UserTemplaateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
