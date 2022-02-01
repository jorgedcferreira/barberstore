from pubsub_library import Subscriber
import smtplib
import json
#import notifications_configs as cfg



#Handler function
def notications_subscriber_handler(message):
    gmail_user = 'thebarberstoreproject@gmail.com'
    gmail_password = 'ADSadsproject'
    sent_from = gmail_user
    print(message)

    print('entrou')
    to = ['thebarberstoreproject@gmail.com']
    subject = 'Welcome to The Barber Store'
    body = 'Welcome to The Barber Store'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        return print ("Email sent successfully!")
    except Exception as ex:
        return print ("Something went wrong….",ex)

notifications_subscriber = Subscriber('NotificationsSubscriber', notications_subscriber_handler)




