from confluent_kafka.avro import AvroProducer
from confluent_kafka.avro.serializer import SerializerError
from random import randint
from random_word import RandomWords

r = RandomWords()

# Define initial schema
value_schema_v1_str = """
{
  "type": "record",
  "name": "RandomSentence",
  "fields": [
    {"name": "id", "type": "int"},
    {"name": "sentence", "type": "string"}
  ]
}
"""

# Load schema from file
with open("schemas/random_sentence_v2.avsc", "r") as f:
    value_schema_str = f.read()

# For schema evolution later, you might add a field:
# {"name": "source", "type": ["null", "string"], "default": null}

kafka_conf = {
    'bootstrap.servers': '192.168.0.253:29092',
    'schema.registry.url': 'http://192.168.0.253:8081'
}

avro_producer = AvroProducer(
    kafka_conf,
    default_value_schema=value_schema_str
)

def generate_random_sentence() -> str:
    sentence_length =  randint(10,20)
    return ' '.join([r.get_random_word() for _ in range(sentence_length)])

count = 1024
while count > 0:
    count -= 1
    value = {
        "id": count,
        "sentence": generate_random_sentence(),
        "score": randint(0, 100)
    }
    try:
        avro_producer.produce(topic='test-topic-avro', value=value)
        avro_producer.flush()
    except SerializerError as e:
        print(f"Serialization error: {e}")
