from redis import Redis
import time

# r = Redis(host='redis-jmwy.sliplane.app', port=6379, password='Q2edJucKQdYtkk5O')
r = Redis(host='localhost', port=6379, password='root')
print(f'Connection status to Redis server: {r.ping()}')  # Should return True


# lets run a loop:


def send_message():
    for i in range(100):
        r.set(f'message_{i}', f'This is message number {i}')
        print(f'Sent message: {i}')
        # sleep for 1 second
        time.sleep(1)
    print('All messages sent!')

def get_message():
    for i in range(100):
        message = r.get(f'message_{i}')
        print(f'Received message: {message.decode("utf-8")}')
        # sleep for 1 second
        time.sleep(1)
    print('All messages received!')


if __name__ == '__main__':
    send_message()

    get_message()

