from confluent_kafka import Producer
from logging import getLogger, StreamHandler
from random import randint
from random_word import RandomWords


r = RandomWords()

mylogger = getLogger()
mylogger.addHandler(StreamHandler())

kafka_conf = {
'bootstrap.servers': 'localhost:9092',
}

producer = Producer(kafka_conf, logger=mylogger)

def generate_random_sentence() -> str:
    sentence_length =  randint(10,20)
    return ' '.join([r.get_random_word() for _ in range(sentence_length)])

count = 10

while count > 0:
    count -= 1
    # send message here
    
    producer.produce(
        topic=f'test-topic',
        value=generate_random_sentence(),
        key=b'i'
    )
    producer.poll()


