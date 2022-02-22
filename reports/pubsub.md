
1. [Introduction](#Introduction)
2. [Patterns used](#Patterns-used)
3. [Use Case](#Use-Case)
4. [UML of classes business](#UML-of-classes-business)
5. [User interfaces](#User-interfaces)
6. [Pubsub and Observer patterns](#Pubsub-and-Observer-patterns)
7. [Conclusions](#Conclusions)


# Introduction

This work is an implementation of the Publisher-Subscriber design pattern within an application of a barber shop management tool. The objective o the work is to explore the capabilities of the Publisher-Subscriber pattern and compare it the Observer pattern. For this purpose the implementation of both patterns was implemented.


# Patterns used

The publish-subscribe pattern is useful for cases in which it is required several independent services or components in distributed way to work with each other, meaning that some action on that services have repercussions on the logic of the other.  For that Publish-Subscribe creates an infrastructure that makes able those components to interact asynchronously through events. That events, that reflect some logic state changes are published by the component in which the alteration occurred, the publisher. That event is then propagated on the Publish-Subscribe infrastructure and the components interested in that event (because it interacts with some of its logic) can consume that event. That component is called the consumer. 
Besides the Publisher-Subscriber,  the Observer pattern implementation was built for the same use case. The big difference between the Publish-Subscribe and the Observer pattern is the coupling level between the event trigger action and the consequence. This happens because the Observer, although having a Publisher and a Subscriber agent as well, the Publisher knows all the Subscribers that are interested on their events and synchronously triggers the messages to the subscribers.


# Use Case

In this specific work, the implementation accounts with several application built in Django Python Server that have some level of independence. The project has a class Person which is a customer of the barber shop, a class Barber and a Class Store. Which one of these classes is a Django app with the same name. Besides those 3 apps we have created a fourth app which is called Notifications which is accountable for managing the logic of sending e-mail notifications to the customers when some relevant event that the customer cares happens. This application has no Template (the component responsible for generating the HTML page on the MTV Django pattern), thus has no user interface associated with it.  On this implementation we focused solely on the event of a customer being created to trigger a welcome e-mail to the customer. Both the Publisher-Subscriber and Observer pattern solved the use case. 


# UML of classes business
![](https://paper-attachments.dropbox.com/s_C1E41D5438AC2C0784F7CEA2B10F49B7C7899C8CC764A5CAFA8873F3CD77A10B_1645533083256_image.png)


The 3 classes above represent the business logic of the barber store. Each one of them with a user interface for CRUD actions. 


# User interfaces

Each one of the classes above mentioned has a menu with UI (User Interfaces) for CRUD actions. The Front-End component was built with the Django MTV pattern, meaning that the client code is retrieved by the server when calling the Django Server API. For he aesthetics of the Front-End was granted by the use of the open-source CSS toolkit bootstrap. Bellow are 3 print screens of the application UIs, a list page of customers (Person objects), a page of creation of Barber objects, and a detail page that enables to edit a given Store object. The delete of an object is made possible both on the list page and on the detail page.  


![](https://paper-attachments.dropbox.com/s_C1E41D5438AC2C0784F7CEA2B10F49B7C7899C8CC764A5CAFA8873F3CD77A10B_1645534482071_image.png)

![](https://paper-attachments.dropbox.com/s_C1E41D5438AC2C0784F7CEA2B10F49B7C7899C8CC764A5CAFA8873F3CD77A10B_1645534494483_image.png)

![](https://paper-attachments.dropbox.com/s_C1E41D5438AC2C0784F7CEA2B10F49B7C7899C8CC764A5CAFA8873F3CD77A10B_1645534512208_image.png)



# Pubsub and Observer patterns

Starting with the Observer pattern, it was created a Python file with the implementation of the pattern classes ([observer_library.py](https://github.com/jorgedcferreira/barberstore/blob/main/observer_library.py)). For that, there were created 3 classes, the Publisher, the Subscriber and a main class Observer. This later class can be used optionally, in alternative to create each one of the Publishers and Subscribers individually by having a configuration as a dictionary, and it is a matter of code style preference. 

On the Observer pattern the Publisher class knows a list of its Subscriber objects, in order to dispatch the events to them. The publisher has 4 public methods: the get_subscribers (to get the list of subscribers), the register (the registration of a  new subscriber), the unregister (to unregister a subscriber) and the dispatch (to dispatch a message or event). On the Subscriber side it only has 2 attributes: a name and a handler, which is a function to handle the events that are dispatched to that Subscriber objetc.

The most important method of this pattern is the dispatch method of the Publisher that uses the get_subscribers of that Publisher and triggers the message to them. After that the handling function of the Subscribers runs synchronously. 

```
    def dispatch(self, event, message):
            for subscriber, subscriber_handler in self.get_subscribers(event).items():
                #@todo Try catch
                message_output = {"event": event,
                                    "message": message
                                    }
                subscriber_handler(message_output)
```

The Publisher-Subscriber pattern implementation has the same Classes Publisher and Subscriber, but the responsibilities of them are slightly different. Besides the Publisher and the Subscriber the class Broker exists and it is necessary for the implementation of the pattern, the Broker is the one responsible for calling the subscribers when an event is published. This happens asynchronously since the events are written on a .csv file  with the topic name and then, a file system observer (using watchdog python library) will track changes on that specific documents and will call the broker to trigger the messages to the subscribers that are consuming that specific topic. 

The implementation of it was as well done on a file called [pubsub_library.py](https://github.com/jorgedcferreira/barberstore/blob/main/pubsub_library.py) and the watchdog file system observer that will call the Broker Object is on the file brokers.py. 

The class broker has a method that calls the subscribers:

```
    def call_subscribers(self, topic, msg):
            for subscriber in self._subscribers: 
                if topic in subscriber.topic:
                    message_output = {"event": topic,
                                    "message": msg
                                    }
                    
                    subscriber_handler = getattr(subscriber, 'subscriber_handler')
                    if subscriber_handler:
                        subscriber_handler(message_output)
                    else:
                        subscriber.sub(message_output)
```

This happens asynchronously when the file system watcher detects an update on a file which in the messages directory:

```
    #file observer
    class MyHandler(FileSystemEventHandler):
        def __init__(self):
            self.last_modified = datetime.now()
        def on_modified(self, event):
            if datetime.now() - self.last_modified < timedelta(seconds=1):
                return
            elif not event.is_directory:
                self.last_modified = datetime.now()
                if event.src_path.rsplit('.',1)[1] == 'csv':
                    print(f'Event type: {event.event_type}  path : {event.src_path}')
                    topic = event.src_path.rsplit('_',1)[0].rsplit('/',1)[1]
                    broker.call_subscribers(topic=topic, msg='test')
    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./pubsub_messages/broker/', recursive=False)
    observer.start()
    try:
        while True:
                time.sleep(1)
    finally:
        observer.stop()
        observer.join()
```

In both implementations the handlers and subscribers must be initiated in the respective application (which for this case is the Notification app) and the publishers must publish the event on the flow of creating a Person which is done on the view of the Person app. 

# Conclusions

In the observer pattern, the source of events itself (the Publisher) knows who are its Subscribers. This means that there is no intermediate broker between Subject and the Subscribers. On the other hand in the pub-sub pattern, the publishers and subscribers are loosely coupled, they are unaware of even the existence of each other. They simply communicate through a broker and the Topic name. 

This makes the observer pattern more indicated to  be implemented in a single-application. On the other hand, the publisher-subscriber pattern is mostly used as a cross-application pattern and is generally used to decouple data/events and systems, i.e., micro-services and event driven architectures. Kafka is a good example of the publish-subscribe pattern. 
