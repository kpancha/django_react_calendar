from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def getCreds():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def addEvent(summary, location, description, startTime, endTime):

    service = build('calendar', 'v3', credentials=getCreds())

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    newEvent = {
      'summary':summary,
      'location':location,
      'description':description,
      'start': {
        'dateTime':startTime.strftime('%Y-%m-%dT%H:%M:%S-04:00'),
      },
      'end': {
        'dateTime':endTime.strftime('%Y-%m-%dT%H:%M:%S-04:00'),
      }
    }
    addedEvent = service.events().insert(calendarId='primary',body=newEvent).execute()
    #print(newEvent.get('summary','a new event') + ' has been added')
    #print('eventId: ' + str(addedEvent['id']))
    
    return addedEvent['id']
'''
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event.get('summary',''))
'''
def updateEvent(eventId, summary, location, description, startTime, endTime):

    service = build('calendar', 'v3', credentials=getCreds())

    event = service.events().get(calendarId='primary', eventId=eventId).execute()

    event['summary'] = summary
    event['location'] = location
    event['description'] = description
    event['start']['dateTime'] = startTime + '-04:00'
    event['end']['dateTime'] = endTime + '-04:00'

    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
    
def deleteEvent(eventId):

    service = build('calendar', 'v3', credentials=getCreds())
    
    service.events().delete(calendarId='primary',eventId=eventId).execute()
    #print('event deleted')
