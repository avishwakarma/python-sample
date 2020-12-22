import datetime
from pony.orm import *

from utils.model import Model

class Story(Model):
  id = PrimaryKey(int, auto=True)
  author = Set('User')
  title = Required(str)
  slug = Required(str, unique=True)
  description = Optional(str)
  content = Required(Json)
  status = Required(bool, sql_default=False)
  created_at = Required(datetime, sql_default='NOW()')