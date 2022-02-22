import pubsub_library as pubsub
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from pathlib import Path
from datetime import datetime, timedelta

broker = pubsub.Broker('broker')

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