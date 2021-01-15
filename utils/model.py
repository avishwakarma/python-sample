from pony.orm import *
from config import LIMIT, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

db = Database()

class Model(db.Entity):
  
  def all(self, params: dict = {}):
    fields = params.fields if params.has_key('fields') else self._columns_
    filter = params.filter if params.has_key('filter') else {}
    order = params.order if params.has_key('order') else {}
    page = params.page if params.has_key('page') else 1

    return self.select(**fields).filter(**filter).order_by(order).page(page, pagesize=LIMIT)[:]

  def one(self, filter: dict = {}):
    return self.get(**filter)

  def delete(self, filter: dict = {}):
    entity = self.one(filter)
    return entity.delete(bulk=True)

db.bind(provider='postgres', user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)
db.generate_mapping(create_tables=True)