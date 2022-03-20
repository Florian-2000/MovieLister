import google.auth.exceptions
import googleapiclient.errors
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Name of key file
SERVICE_ACCOUNT_FILE = '../resources/key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of the spreadsheet.
SPREADSHEET_ID = ''

# The range name to be read
RANGE_NAME = ''

# table cells
TITLE_CELL = 0
GENRE_CELL = 1
LENGTH_CELL = 2
CHECKBOX_CELL = 3

service = build('sheets', 'v4', credentials=creds)


# Call Sheet
def get_list_from_sheet():
    try:
        sheet = service.spreadsheets()
        # Save results as list in list
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        # Save only data of sheets
        values = result.get('values', [])

        # If there is no data
        if len(values) == 0:
            print('No Data found. Add entries to your list or check if the table name and range is correct.')
            quit()

        print('Connection successful!')
        return values
    # If connection to sheet failed
    except googleapiclient.errors.HttpError:
        print('The Sheet ID does not exist')
        quit()
    except google.auth.exceptions.TransportError:
        print('Connection to server failed. Check your internet connection or try it later.')
        quit()

