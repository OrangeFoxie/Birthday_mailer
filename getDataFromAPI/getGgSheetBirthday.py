from __future__ import print_function
import sys
sys.path.append(r'.\CustomConfig')
from accountConfig import googleSetup
from googleapiclient.discovery import build
from google.oauth2 import service_account

gg = googleSetup() 

SERVICE_ACCOUNT_FILE = gg['service_account_file']
SCOPES = gg['scopes']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = gg['sample_spreadsheet_id']
SAMPLE_RANGE_NAME = gg['sample_range_name']

def Values():
    service = build('sheets', 'v4', credentials=creds)
    arr = []

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            arr.append([row[0],row[1],row[2], row[3]])
        return(arr)