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

    # Remove 1 to 5
    assert q.get() == 1
    assert q.get() == 2
    assert q.get() == 3
    assert q.get() == 4
    assert q.get() == 5

def main():
    Queue()

if __name__ == '__main__':
    main()
    print('Tests passed!')
