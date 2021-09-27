from __future__ import print_function
import re,sys
sys.path.insert(0, './config')
from configMailer import googleSetup
from googleapiclient.discovery import build
from google.oauth2 import service_account

ggSetup = googleSetup()

SERVICE_ACCOUNT_FILE = ggSetup['service_account_file']
SCOPES = ggSetup['scope']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ggSetup['sample_spreadsheet_id']
SAMPLE_RANGE_NAME = ggSetup['sample_range_name']

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

# if __name__ == '__main__':
#     main()