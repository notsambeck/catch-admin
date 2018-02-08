import anvil.users
import tables
from tables import app_tables
import anvil.server

@anvil.server.callable
def get_user_action_counts(user):
  return len(app_tables.user_actions.search(user=user))
