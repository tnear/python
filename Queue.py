# Queue: implements multi-producer, multi-consumer queues.
# It is useful in threaded programming when information
# must be exchanged safely between multiple threads.
# https://docs.python.org/3/library/queue.html

import queue

def Queue():
    q = queue.Queue()

    # Insert 1 to 5
    for i in range(1, 6):
        q.put(i)

    assert not q.empty()

    # Remove 1 to 5
    assert q.get() == 1
    assert q.get() == 2
    assert q.get() == 3
    assert q.get() == 4
    assert q.get() == 5
    assert q.qsize() == 0
    assert q.empty()

def MinPriorityQueue():
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

def main():
    Queue()
    MinPriorityQueue()

if __name__ == '__main__':
    main()
    print('Tests passed!')
