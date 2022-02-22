import csv
import os

#configs
pubsub_base_folder_path = 'pubsub_messages'

class Broker(object):
    """
    Broker
    """
    def __init__(self, name=''):
        self._name = name
        self._subscribers = []
        self.files_watched = []
        self.file_observers = []


    def attach(self, subscriber):
        """"""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def detach(self, subscriber):
        """"""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def route(self, msg, topic=''):
        """"""
        topic_file_path, topic_offset_file_path = self.__validate_files_and_directories(topic)

        #Writting event in file
        with open(topic_file_path, 'a+', newline='', encoding="UTF8") as file:
            with open(topic_offset_file_path) as offset_file:
                offset = int(offset_file.read())
                offset_file.close()
            csv_writer = csv.writer(file)
            offset += 1
            data = [offset,str(msg)]
            csv_writer.writerow(data)
            with open(topic_offset_file_path, 'w') as offset_file:
                offset_file.write(str(offset))
                offset_file.close()
        print('vou a ver os meus subs')
    
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

    

    def __validate_files_and_directories(self, topic):
        #File and brokers paths
        topic_file_path = './{}/{}/{}_topic.csv'.format(pubsub_base_folder_path , self._name, topic)
        topic_offset_file_path = './{}/{}/{}_topic_offset.txt'.format(pubsub_base_folder_path ,self._name, topic)
        broker_folder_path = '{}/{}'.format(pubsub_base_folder_path,self._name)

        #Check if broker messages directory and file exist
        chek_base_folder = os.path.isdir(pubsub_base_folder_path)
        check_topic_file = os.path.exists(topic_file_path)
        check_topic_offset_file = os.path.exists(topic_offset_file_path)


        #Create base and broker directory if not exists
        if not chek_base_folder:
            os.makedirs(pubsub_base_folder_path)
            print("created folder : ", pubsub_base_folder_path)
            check_broker_folder = os.path.isdir(broker_folder_path)
            
            if not check_broker_folder:
                os.makedirs(broker_folder_path)
                print("created folder : ", broker_folder_path)

        #Create files if not exists
        if not check_topic_file:
            with open(topic_file_path, 'w') as file:
                writer = csv.writer(file)
                header = ['event_id', 'message']
                writer.writerow(header)
                print('{} file created'.format(topic_file_path))
                file.close()
            

        if not check_topic_offset_file:
            with open(topic_offset_file_path, 'w') as file:
                file.write('0')
                file.close()


        return topic_file_path, topic_offset_file_path


class Publisher(object):
    """Publisher"""
    def __init__(self, name, broker):
        self._name = name
        self._broker = broker

    def pub(self, msg, topic=''):
        print('[Publisher: {}] topic: {}, message: {}'.format(self._name, topic, msg))  
        self._broker.route(msg, topic)


class Subscriber(object):
    """Subscriber"""
    def __init__(self, name, broker, topic=None, subscriber_handler= None):
        self._name = name
        broker.attach(self)
        self._topic = [] if topic is None else topic
        self.subscriber_handler = subscriber_handler

    def sub(self, msg):
        print('[Subscriber: {}] got message: {}'.format(self._name, msg))

    @property   
    def topic(self):
        return self._topic


def main():
    broker = Broker('broker')

    
    p1 = Publisher('p1', broker)
    p2 = Publisher('p2', broker)

    def s1_handler(message):
        print(message)

    s1 = Subscriber('s1', broker, topic=['A'], subscriber_handler=s1_handler)
    s2 = Subscriber('s2', broker, topic=['A', 'B'])
    
    p1.pub('hello s1', topic='A')
    p2.pub('hello s2', topic='B')


if __name__ == '__main__':
    main()