import observer_library as observer

#Import events
from person.events import person_events

#Import Subscribers
from notifications.subscribers import notifications_subscriber



person_publisher = observer.Publisher(person_events)
person_publisher.register(event='PersonCreatedEvent', subscriber=notifications_subscriber)