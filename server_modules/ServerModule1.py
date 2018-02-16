import anvil.users
import tables
from tables import app_tables
import anvil.server
from datetime import datetime

from collections import defaultdict

@anvil.server.callable
def get_user_action_counts(user):
  return len(app_tables.user_actions.search(user=user))

@anvil.server.callable
def get_traffic():
  '''
  gets a dictionary:
  {time bucket (hour): number of actions in bucket}
  '''
  out = defaultdict(0)
  now = datetime.utcnow()
  data = app_tables.user_actions.search(tables.order_by('time', ascending=False))
  for row in data:
    out[(now - row['time']).hours] += 1
    
  return out