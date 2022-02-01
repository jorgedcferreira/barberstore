import pubsub_library as pubsub
from barber.subscribers import barber_subscribber


#subscriber functions
def custom_handler_test(message):
    print('correu bem')



# #PubSubConfig
pubsub_config = {
    'topic_subscribers':
    [
        {'event': 'PersonCreatedEvent',
        'subscribers': [
                        {'subscriber_name': barber_subscribber.name,
                        'handler': custom_handler_test
                         }
                    ]
        },
        {'event': 'PersonCreatedEvent2',
        'subscribers': [
                        {'subscriber_name': barber_subscribber.name,
                        'handler': custom_handler_test
                         }
                    ]
        },
    ]
}

#Initialize observer
observer = pubsub.Observer(pubsub_config)