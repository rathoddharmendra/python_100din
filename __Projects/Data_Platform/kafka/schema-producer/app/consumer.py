from confluent_kafka import Consumer, KafkaException, KafkaError
from conn import generate_cursor

# Kafka consumer configuration
conf = {
    'bootstrap.servers': '192.168.0.253:29092',  # Change if using a remote broker
    'group.id': 'test-consumer-group-01',
    'auto.offset.reset': 'earliest',  # Start from beginning if no previous offset exists
    'enable.auto.commit': False,          # Disable auto commit to manually control offsets

}

# Create consumer instance
consumer = Consumer(conf)
cursor, con = generate_cursor()

# Subscribe to the 'test' topic
consumer.subscribe(['test-topic'])

print("Consumer is listening for messages on 'test' topic...")

try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Wait for message

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of partition")
            else:
                raise KafkaException(msg.error())

        # Print received message
        try:
            print(f"Received message: {msg.value().decode('utf-8')}")
            data = msg.value().decode('utf-8')
        # cursor.execute(f'insert into dumps values({len(data)}, {data[0]})')
            cursor.execute('INSERT INTO dumps VALUES (?, ?)', (len(data), data))
            con.commit()
        except Exception as e:
            print(f"Error processing message: {e}")
            cursor.execute('INSERT INTO dumps VALUES (?, ?)', (0, str(e)))
            con.commit()

except KeyboardInterrupt:
    print("\nClosing consumer...")
finally:
    consumer.close()
    con.close()
