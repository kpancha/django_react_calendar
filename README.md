# django_react_calendar
Configure app with Google Calendar API:
- Enable the Google Calendar API here: https://developers.google.com/calendar/quickstart/python?authuser=1#step_1_turn_on_the 
  - save `credentials.json` to your working directory
- Install Google Client Library:

  `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

Run app:
- Create and activate a Python virtual environment:

  `python -m venv venv` 
  
  `source venv/bin/activate`
- Install dependencies:

  `pip install django djangorestframework`

- Make migrations:

  `python manage.py makemigrations`
  
  `python manage.py migrate`

- Run the app:

  `python manage.py runserver`
