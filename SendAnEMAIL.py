#v1 - gmail - needs app password to send.txt

#needed gmail app password - to send
# (https://www.interviewqs.com/blog/py-email)

import smtplib, ssl

def sendAnEMAIL(message_body,subject1,to_who,from_who):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "myvortexlife1012@gmail.com"  # Enter your address
    receiver_email = "myvortexlife1012@gmail.com"  # Enter receiver address
    app_password = "tavpwbeipnoggquz"
    password = app_password #input("Type your password and press enter: ")
    if subject1=="":
        subject1 = "Test Subject in Python - 1"
    if message_body=="":
        message = """\
    Subject: {subject}
    
    This message is sent from Python.""".format(subject=subject1)
    else:
        message = message_body
    #
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message, subject)



to_who = "myvortexlife1012@gmail.com"  # Enter receiver address
from_who = to_who
body = "Test python email message body ... cool"
subject = "Test Subject in Python - 1"
sendAnEMAIL(body,subject,to_who,from_who)