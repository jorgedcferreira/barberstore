from itertools import chain 


class Subscriber():
    def __init__(self, name, subscriber_handler=None):
        self.name = name
        self.subscriber_handler = subscriber_handler

    def default_handler(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict()
                            for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, subscriber, subscriber_handler=None):
        if subscriber_handler is None and getattr(subscriber, 'subscriber_handler') != None:
            subscriber_handler = getattr(subscriber, 'subscriber_handler')
        else:
            subscriber_handler = getattr(subscriber, 'default_handler')
        self.get_subscribers(event)[subscriber] = subscriber_handler
        
    def unregister(self, event, subscriber):
        del self.get_subscribers(event)[subscriber]
    
    def dispatch(self, event, message):
        for subscriber, subscriber_handler in self.get_subscribers(event).items():
            #@todo Try catch
            message_output = {"event": event,
                                "message": message
                                }
            subscriber_handler(message_output)


class Observer:
    def __init__(self, pubsub_config):
        self.pub = Publisher(events=[topic['event'] for topic in pubsub_config['topic_subscribers']])
        self.subscribers = {}

        for subscriber_name in list(dict.fromkeys([subscriber['subscriber_name'] for subscriber in list(chain.from_iterable([topic['subscribers'] for topic in pubsub_config['topic_subscribers']]))])):
            self.subscribers[subscriber_name]= Subscriber(subscriber_name)
        
        for topic in pubsub_config['topic_subscribers']:
            for subscriber in topic['subscribers']:
                self.pub.register(topic['event'], self.subscribers[subscriber['subscriber_name']], subscriber['handler'])

    def dispatch(self, event, message):
            self.pub.dispatch(event, message)

    def register_subscriber(self, subscriber_name, handler=None):
        self.subscribers[subscriber_name]= Subscriber(subscriber_name, handler)
    
    def unregister_subscriber(self, event, subscriber_name):
        del self.pub.get_subscribers(event)[subscriber_name]

