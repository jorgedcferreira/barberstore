from re import sub
import pubsub_library as pubsub

#Import events
from person.events import person_events

#Import Subscribers
from notifications.subscribers import notifications_subscriber



person_publisher = pubsub.Publisher(person_events)
person_publisher.register(event='PersonCreatedEvent', subscriber=notifications_subscriber)