import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from CustomConfig import configMailer 

def infoMailer():   
    configmailer = configMailer.mailSetup()

    port = configmailer['port']  # For starttls
    smtp_server = configmailer['smtp_server']
    sender_email = configmailer['sender_email']
    receiver_email = configmailer['receiver_email']
    password = configmailer['password']

    return {
        'port':port, 
        'smtp_server':smtp_server, 
        'sender_email':sender_email, 
        'receiver_email':receiver_email, 
        'password':password
        }



# Get date time
def getDate():
    getDate = date.today()
    today = getDate.strftime("%d-%m-%G")
    return {'today':today}


# Mail data
def mailData(sender_email,receiver_email,today):
    message = MIMEMultipart("alternative")
    message["Subject"] = "CHÚC MỪNG SINH NHẬT"
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_email)
    text = """\
        Chào bạn!
        Mail này được gửi tự động đến bạn.
        Hôm nay là {TODAY}
        CHÚC BẠN MỘT NGÀY SINH NHẬT VUI VẺ
        """
    html = """\
    <html>
    <body>
        <p>Chào bạn!<br>
        Mail này được gửi tự động đến bạn.<br>        
        Hôm nay là {TODAY}.
        CHÚC BẠN MỘT NGÀY SINH NHẬT VUI VẺ
        <a href="https://github.com/OrangeFoxie/Birthday_mailer.git">Gấu mèo</a> 
        </p>
    </body>
    </html>
    """
    new_html = html.format(TODAY=today)
    new_text = text.format(TODAY=today)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(new_text, "plain")
    part2 = MIMEText(new_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    return {'message': message}


    
def sendMail(smtp_server,sender_email,receiver_email,password,port,message):
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
        sender_email, receiver_email, message.as_string()
    )



# main function
def main():
    ifm = infoMailer()
    today = getDate()
    message = mailData(ifm['sender_email'],ifm['receiver_email'],today['today'])
    
    mailData(
            ifm['sender_email'],
            ifm['receiver_email'],
            today['today']
            )
    sendMail(
            ifm['smtp_server'],
            ifm['sender_email'],
            ifm['receiver_email'],
            ifm['password'],
            ifm['port'],
            message['message'],            
            )


main()