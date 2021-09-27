import sys, getpass
sys.path.append(r'.\StoreData')
from storeBirthday import getUserEmailList

usrEmail = getUserEmailList()

def mailSetup():
    port = 465  # For starttls
    smtp_server = 'smtp.gmail.com'
    sender_email = 'vinhphuc931998@gmail.com'
    receiver_email = usrEmail
    password = getpass.getpass("Type your email password to send: ")
    return {
    'port':port, 
    'smtp_server':smtp_server, 
    'sender_email':sender_email, 
    'receiver_email':receiver_email, 
    'password':password
    }

def googleSetup():
    service_account_file = '.\keyAPI\getUserBirthday\service.json'
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    sample_spreadsheet_id = '1gINjp6tlqbd2XN2jgWjlQ-qKTKo3K8LIDJHjwIkpX1I'
    sample_range_name = 'BirthDay!A2:D'
    return {
        'service_account_file':service_account_file,
        'scope':scope,
        'sample_spreadsheet_id':sample_spreadsheet_id,
        'sample_range_name':sample_range_name
    }