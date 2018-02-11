import anvil.users
import tables
from tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def get_user_action_counts(user):
  return len(app_tables.user_actions.search(user=user))

def get_user_actions():
  '''
  gets a dictionary of user actions:
  
  '''
  