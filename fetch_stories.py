from pony.orm import *
from utils.session import Session
from utils.response import Response
from models.Story import Story

def fetch_stories(event, context):
  user = Session.user(event.headers['Authorization'])

  if(not bool(user)):
    return Response(401, {
      'status': False,
      'message': 'Unauthorized! Invalid or missing Auth token.'
    }).toJson()

  filter: dict = {}

  if(event.queryStringParameters.has_key('status')):
    filter['status'] = event.queryStringParameters['status']

  if(event.queryStringParameters.has_key('q')):
    filter['title'] = Story.title.startswith(event.queryStringParameters['q'])

  filters = event.queryStringParameters
  stories = Story.all({
    'filter': filter
  })
    
  return Response(200, {
    'status': True,
    'data': stories
  }).toJson()