from redis import Redis
import time
import json

# r = Redis(host='redis-jmwy.sliplane.app', port=6379, password='Q2edJucKQdYtkk5O')
r = Redis(host='localhost', port=6379, password='root')
print(f'Connection status to Redis server: {r.ping()}')  # Should return True

# lets run a loop:


def send_message():
    for i in range(100):
        r.set(f'message_{i}', f'This is message number {100 - i}')
        print(f'Sent message: {i}')
        # sleep for 1 second
        # time.sleep(1)
    print('All messages sent!')

def get_message():
    for i in range(100):
        message = r.get(f'message_{i}')
        print(f'Received message: {message.decode("utf-8")}')
        # sleep for 1 second
        # time.sleep(1)
    print('All messages received!')


if __name__ == '__main__':
    send_message()

    get_message()

data = {'name': 'Alice', 'age': 30}
r.set('user:1001', json.dumps(data))

# Retrieve and parse
user_data = json.loads(r.get('user:1001'))
print(user_data['name'])  # Alice


# List
r.rpush('tasks', 'task1')
r.rpush('tasks', 'task2')
print(r.lrange('tasks', 0, -1))  # [b'task1', b'task2']

# Hash
r.hset('user:1', mapping={'name': 'John', 'age': 28})
print(r.hgetall('user:1'))  # {b'name': b'John', b'age': b'28'}