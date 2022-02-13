from observer_library import Subscriber
import smtplib
import json
#import notifications_configs as cfg
from pubsub_library import Subscriber as pubsub_Subscriber
from brokers import broker



#Handler function
def notications_subscriber_handler(message):
    gmail_user = 'thebarberstoreproject@gmail.com'
    gmail_password = 'ADSadsproject'
    sent_from = gmail_user
    
    to = ['thebarberstoreproject@gmail.com']
    subject = 'Welcome to The Barber Store'
    body = 'Welcome to The Barber Store'

    print('isto correu bem')

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

notifications_pubsub_subscriber = pubsub_Subscriber(name='NotificationsSubscriber', broker=broker, topic=['PersonCreatedEvent'], subscriber_handler=notications_subscriber_handler)

