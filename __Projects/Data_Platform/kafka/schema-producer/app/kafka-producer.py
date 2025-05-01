from confluent_kafka import Producer
from logging import getLogger, StreamHandler
from random import randint
from random_word import RandomWords


r = RandomWords()

mylogger = getLogger()
mylogger.addHandler(StreamHandler())

kafka_conf = {
'bootstrap.servers': '192.168.0.253:29092',
}

producer = Producer(kafka_conf, logger=mylogger)

def generate_random_sentence() -> str:
    sentence_length =  randint(10,20)
    return ' '.join([r.get_random_word() for _ in range(sentence_length)])

count = 1024

while count > 0:
    count -= 1
    # send message here

    value = {
        "id": count,
        "sentence": generate_random_sentence(),
        "score": randint(0, 100)
    }
    
    producer.produce(
        topic=f'test-topic',
        value=f'{value}',
        key=f'{count}',
    )
    producer.poll()


