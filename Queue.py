# Queue: A synchronized queue class
# Implements multi-producer, multi-consumer queues.
# It is useful in threaded programming when information
# must be exchanged safely between multiple threads.
# https://docs.python.org/3/library/queue.html

import queue
import threading
import time
import random

def Queue():
    q = queue.Queue()

    # Insert 1 to 5
    for i in range(1, 6):
        q.put(i)

    assert not q.empty()

    # get() returns and removes the oldest element in the queue.
    # Remove 1 to 5:
    assert q.get() == 1
    assert q.get() == 2
    assert q.get() == 3
    assert q.get() == 4
    assert q.get() == 5
    assert q.qsize() == 0
    assert q.empty()

def minPriorityQueue():
    pq = queue.PriorityQueue()

    # Insert in random order
    pq.put(3)
    pq.put(2)
    pq.put(5)
    pq.put(4)
    pq.put(1)

    # Verify removes happen lowest to highest
    assert pq.get() == 1
    assert pq.get() == 2
    assert pq.get() == 3
    assert pq.get() == 4
    assert pq.get() == 5

def size():
    # Queue size / length
    q = queue.Queue()
    assert q.qsize() == 0

    q.put(1)
    assert q.qsize() == 1

    q.put(1)
    assert q.qsize() == 2

# Constants
NUM_PRODUCERS = 2
NUM_CONSUMERS = 2
QUEUE_SIZE = 5
NUM_ITEMS_PER_PRODUCER = 10

# Shared Queue
q = queue.Queue(QUEUE_SIZE)

# Producer function
def producer():
    for _ in range(NUM_ITEMS_PER_PRODUCER):
        item = random.randint(0, 100)
        print(f'{threading.current_thread().name} producing {item}')
        q.put(item)  # This will block if the queue is full
        time.sleep(random.uniform(0.01, 0.1))

# Consumer function
def consumer():
    while True:
        item = q.get()  # This will block if the queue is empty
        if item is None:  # Sentinel value to exit
            break
        print(f'{threading.current_thread().name} consuming {item}')
        time.sleep(random.uniform(0.01, 0.1))

def producerConsumer():
    # Create and start producer threads
    producer_threads = []
    for _ in range(NUM_PRODUCERS):
        t = threading.Thread(target=producer, name=f'Producer-{_}')
        t.start()
        producer_threads.append(t)

    # Create and start consumer threads
    consumer_threads = []
    for _ in range(NUM_CONSUMERS):
        t = threading.Thread(target=consumer, name=f'Consumer-{_}')
        t.start()
        consumer_threads.append(t)

    # Wait for all producers to finish producing
    for t in producer_threads:
        t.join()

    # Since our consumers are running in infinite loops,
    # we'll send a sentinel value to signal them to exit
    for _ in range(NUM_CONSUMERS):
        q.put(None)

    # Wait for all consumers to finish consuming
    for t in consumer_threads:
        t.join()

def main():
    Queue()
    minPriorityQueue()
    size()
    producerConsumer()

if __name__ == '__main__':
    main()
    print('Tests passed!')
