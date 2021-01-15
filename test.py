import json
from utils.model import Model

data = '''{
  "name": "User",
  "fields": {
    "id": {
      "type": "integer",
      "primary": true,
      "autoGenerate": true
    },
    "firstName": {
      "type": "string",
      "required": true
    },
    "lastName": {
      "type": "string",
      "required": true
    },
    "email": {
      "type": "string",
      "required": true,
      "unique": true
    },
    "password": {
      "type": "string",
      "required": true
    },
    "location": {
      "type": "string"
    },
    "status": {
      "type": "boolean",
      "defult": false
    },
    "created_at": {
      "type": "datetime",
      "sql_default": "NOW()"
    }
  }
} '''

class Schema(Model):
  config = None
  
  def __init__(self, config: any = {}):
    self.config = json.loads(config)
      
    for key, value in self.config['fields'].items():
      setattr(self, key, True)
        
        
schema = Schema(data)

print(schema.firstName)