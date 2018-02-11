from anvil import *
import anvil.server
import anvil.users
import tables
from tables import app_tables
from datetime import datetime

class UserTemplaate (UserTemplaateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

  def form_show (self, **event_args):
    # This method is called when the column panel is shown on the screen
    my_actions = self.parent.parent.actions.search(user=self.item)
    
    account_created = self.item['account_created']
    self.throws_label.text = len(my_actions)
    
    time_active = 0
    for action in my_actions:
      delta = (action['time'] - account_created).days
      if delta > time_active:
        time_active = delta
    self.date_label.text = 'time active: {} days'.format(time_active)
    
    self.logins_label.text = len(self.parent.parent.actions.search(user=self.item, action_type='login'))
