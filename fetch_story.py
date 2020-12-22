from pony.orm import *
from utils.session import Session
from utils.response import Response
from models.Story import Story

def fetch_story(event, context):
  user = Session.user(event.headers['Authorization'])

  if(user is None):
    return Response(401, {
      'status': False,
      'message': 'Unauthorized! Invalid or missing Auth token.'
    }).toJson()

  id: str = event.queryStringParameters['id']

  if(not bool(id)):
    return Response(404, {
      'status': False,
      'message': 'URL does not exists'
    }).toJson()

  story = Story.one({'id': id})
    
  return Response(200, {
    'status': True,
    'data': story
  }).toJson()