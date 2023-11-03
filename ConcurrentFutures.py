# concurrent.futures — Launching parallel tasks
# https://docs.python.org/3/library/concurrent.futures.html

import concurrent.futures
import contextlib
import time

# https://youtu.be/6g79qGQo2-Q
@contextlib.contextmanager
def timeIt(what: str):
    t0 = time.monotonic()
    try:
        yield
    finally:
        print(f'{what} took {time.monotonic() - t0}')

def doWork():
    # create some cpu-bound work
    with timeIt('doWork'):
        x = 0
        for _ in range(2_000_000):
            x += 1

        return x

# takes about 1 second
def threadPoolExecutor():
    with timeIt('main'):
        # 4 workers: doWork takes about 0.3 seconds
        # 1 worker : doWork takes about 0.1 seconds
        # this is because doWork is cpu-bound and context switching the threads
        # reduces the amount of time available for work. The GIL only allows one
        # thread to run at a time.
        # threads in python are better for I/O-bound tasks
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(doWork) for _ in range(10)]

            # use as_completed() to get results
            for future in concurrent.futures.as_completed(futures):
                print(f'got {future.result()}')

# same as threadPoolExecutor but uses ProcessPoolExecutor
# to create multiple processes instead of threads
# takes about 0.4 seconds
def processPoolExecutor():
    with timeIt('main'):
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(doWork) for _ in range(10)]

def main():
    threadPoolExecutor()
    processPoolExecutor()

if __name__ == '__main__':
    main()
    print('Tests passed!')
