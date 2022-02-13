from brokers import broker
import pubsub_library as pubsub 

person_events = ['PersonCreatedEvent']
PersonPublisher = pubsub.Publisher('PersonPublisher', broker)
