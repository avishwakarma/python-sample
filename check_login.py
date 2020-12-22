from utils.session import Session
from utils.response import Response

def check_login(event, context):
  user = Session.user(event.headers['Authorization'])

  if(not bool(user)):
    return Response(401, {
      'status': False,
      'message': 'Unauthorized! Invalid or missing Auth token.'
    }).toJson()
    
  return Response(200, {
    'status': True,
    'message': 'Authorised.'
  }).toJson()