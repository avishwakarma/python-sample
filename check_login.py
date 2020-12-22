from utils.session import Session
from utils.response import Response

def check_login(event, context):
  isValid = Session.check(event.headers['Authorization'])

  if(isValid is not True):
    return Response(401, {
      'status': False,
      'message': 'Unauthorized! Invalid or missing Auth token.'
    }).toJson()
    
  return Response(200, {
    'status': True,
    'message': 'Authorised.'
  }).toJson()