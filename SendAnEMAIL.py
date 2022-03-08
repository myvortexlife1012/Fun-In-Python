#v1 - gmail - needs app password to send.txt

#needed gmail app password - to send
# (https://www.interviewqs.com/blog/py-email)

"""
to_who = "myvortexlife1012@gmail.com"  # Enter receiver address
from_who = to_who
body = "Test python email message body ... cool"
subject = "Test Subject in Python - 1"
# import SendAnEMAIL as e
e.sendAnEMAIL(body,subject,to_who,from_who)
"""

# import SendAnEMAIL as email
# email.sendAnEMAIL(message_body,subject1,to_who,from_who)

#doesn't send a subject
def sendAnEMAIL(messageBody="Test Body Message",subject1="Test Subject",to_who="a@b.com",from_who="b@c.com"):
    print(f"subject1: {subject1}")
    import smtplib, ssl
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = from_who # "myvortexlife1012@gmail.com"  # Enter your address
    receiver_email = to_who # "myvortexlife1012@gmail.com"  # Enter receiver address
    app_password = "tavpwbeipnoggquz"
    password = app_password #input("Type your password and press enter: ")
    if subject1=="":
        subject1 = "Test Subject in Python - 1"
    if messageBody=="":
        message = """\
    Subject: {subject}
    
    This message is sent from Python.""".format(subject=subject1)
    else:
        message = messageBody
    #
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message, subject1)


def sendEmail3(messageBody="Test Body Message",subject1="Test Subject",to_who="a@b.com",from_who="b@c.com"):
    import smtplib

    msg = """From: hello@hello.com
    To: hi@hi.com\n
    Subject: <Subject goes here>\n
    Here's my message!\nIt is lovely!
    """

    server = smtplib.SMTP_SSL('smtp.example.com', port=465)
    server.set_debuglevel(1)
    server.ehlo
    server.login('examplelogin', 'examplepassword')
    server.sendmail('me@me.com', ['anyone@anyone.com '], msg)
    server.quit()



# uses MIMEMultipart() to send the email
def sendEmail2(messageBody="Test Body Message",subject1="Test Subject",to_who="a@b.com",from_who="b@c.com"):
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    import smtplib

    msg = MIMEMultipart()
    msg['From'] = f = from_who # "myvortexlife1012@gmail.com" # 'EMAIL_USER'
    msg['To'] = t = to_who # "myvortexlife1012@gmail.com" # 'EMAIL_TO_SEND'
    msg['Subject'] = s = subject1 # "Test Subject from Python" # 'SUBJECT'

    body = messageBody # "Test Reminder from Python. Remember to do the thing." # 'YOUR TEXT'
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    app_password = "tavpwbeipnoggquz"
    server.login("myvortexlife1012@gmail.com", app_password)
    server.sendmail(f, t, text)
    server.quit()