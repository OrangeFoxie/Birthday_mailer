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