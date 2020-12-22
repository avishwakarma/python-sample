import datetime
from pony.orm import *

from utils.model import Model

class User(Model):
  id = PrimaryKey(int, auto=True)
  firstName = Required(str)
  lastName = Required(str)
  email = Required(str, unique=True)
  password = Required(str)
  location = Optional(str)
  status = Required(bool, sql_default=False)
  created_at = Required(datetime, sql_default='NOW()')