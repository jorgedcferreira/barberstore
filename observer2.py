import observer_library as observer
from notifications.subscribers import notifications_subscriber


# #PubSubConfig
observer_config = {
    'topic_subscribers':
    [
        {'event': 'PersonCreatedEvent',
        'subscribers': [
                        {'subscriber_name': notifications_subscriber.name,
                        'handler': notifications_subscriber.subscriber_handler
                         }
                    ]
        },
        {'event': 'PersonCreatedEvent2',
        'subscribers': [
                        {'subscriber_name': notifications_subscriber.name,
                        'handler': notifications_subscriber.subscriber_handler
                         }
                    ]
        },
    ]
}

#Initialize observer
observer = observer.Observer(observer_config)