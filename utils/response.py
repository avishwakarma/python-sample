from json import decoder, encoder

class Response():
  _body = None
  _code = None
  _headers = {'Content-Type': 'application/json'}

  _contentType = 'application/json'

  def __init__(self, code: int, body: dict, headers: dict = {}):
    self._body = encoder(body)
    self._code = code
    self._headers = self._headers.update(headers)

  
  def toJson(self):
    return encoder({
      'statusCode': self._code,
      'body': self._body,
      'headers': self._headers
    })
    
