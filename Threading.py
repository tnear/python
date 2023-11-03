# Thread-based parallelism
# https://docs.python.org/3/library/threading.html
# https://realpython.com/intro-to-python-threading/
# Threads run one at a time and are context switched by the CPU.
# Threads are most beneficial for IO-bound applications.
# (CPU-bound computations might not benefit from threading)

# Global Interpreter Lock (GIL): a lock in Python that allows only
# one thread to hold the control of the Python interpreter. In other
# words, only one thread can be executing at at time. GIL exists
# because Python is a reference-counted language. Although having
# locks around every variable would work, it would hurt performance.
# Instead, it was decided to have one global lock, the GIL.

# Note: time.sleep drops the GIL

import threading
import concurrent.futures
import logging
import requests
import time

def _threadFunction(arg1, arg2):
    print(f'Running in a thread with args: {arg1} {arg2}')

    # get thread's identity (a non-negative integer)
    print(f'Thread identity: {threading.get_ident()}')

def threadCreation():
    # associate thread with _threadFunction
    thread = threading.Thread(target=_threadFunction, args=('hello', 'world'))

    # start thread
    thread.start()
    thread.join()

def daemonThread():
    # a daemon thread is a thread which shuts down as soon as the
    # the main program completes. The program does not wait for
    # a daemon thread to finish processing
    thread = threading.Thread(target=_threadFunction, args=(1,2), daemon=True)
    thread.start()

def threadPoolExecutor():
    # a thread pool executor is a useful way to create multiple threads

    # they are typically used in a context manager. The end of the 'with statement
    # calls 'join' on all the threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(_threadFunction, range(3))

class _DatabaseNotThreadSafe:
    def __init__(self):
        self.value = 0

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

def raceCondition():
    database = _DatabaseNotThreadSafe()
    assert database.value == 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info('Testing update. Ending value is %d.', database.value)

    #assert database.value == 2
    assert database.value == 1
    # the database value should be 2 after creating 2 threads and incrementing 0 twice
    # however, the value is 1 due to a race condition. Both threads are mutating
    # the shared self.value variable at the same time

# corrected version of database which uses a lock to wrap shared data updates
class _DatabaseThreadSafe:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

# lock = threading.Lock()
# locks have acquire and release methods, but generally should be used in a context manager
def lock():
    database = _DatabaseThreadSafe()
    assert database.value == 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info('Testing update. Ending value is %d.', database.value)

    assert database.value == 2

def _helloFunction():
    print('Hello from the timer!')

def timer():
    # create a timer which waits 0.12 seconds
    t = threading.Timer(0.12, _helloFunction)

    # start the timer. This will output the string after the countdown elapses
    t.start()

    # [optional] cancel timer
    # t.cancel()

def _worker(num, semaphore):
    # thread worker function
    print(f'Thread {num} is waiting for the semaphore...')
    with semaphore:
        print(f'Thread {num} has acquired the semaphore!')
        time.sleep(.15)  # Simulate some work
        print(f'Thread {num} is releasing the semaphore...')

def semaphore():
    # a semaphore is used to control access to a resource to a limited quantity

    # create a semaphore that allows up to 2 threads to execute concurrently
    semaphore = threading.Semaphore(2)

    # create 5 workers. The semaphore enforces that at most 2 will be active at a time
    maxWorkers = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
        # note: all arguments to map must be the same length, hence the semaphore list
        executor.map(_worker, range(maxWorkers), [semaphore] * maxWorkers)

# create thread-local data
threadLocal = threading.local()

def getSession():
    # create one requests session per thread
    # (creating one session per function call is unnecessarily slow)
    if not hasattr(threadLocal, 'session'):
        threadLocal.session = requests.Session()
    return threadLocal.session

def downloadSite(url):
    session = getSession()
    with session.get(url) as response:
        print(f'Read {len(response.content)} bytes from {url}')

def downloadAllSites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(downloadSite, sites)

def local():
    # this example uses threading.Local to create one requests session per thread
    # by downloading sites is parallel (which is IO-bound), this should improve performance
    sites = ['https://www.jython.org', 'http://olympus.realpython.org/dice'] * 20
    startTime = time.time()
    downloadAllSites(sites)
    duration = time.time() - startTime
    print(f'Downloaded {len(sites)} sites in {duration} seconds!')

def main():
    threadCreation()
    daemonThread()
    threadPoolExecutor()
    raceCondition()
    lock()
    timer()
    semaphore()
    local()

if __name__ == '__main__':
    main()
    print('Tests passed!')
