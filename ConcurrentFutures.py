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
    with timeIt('threadPoolExecutor'):
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
    with timeIt('processPoolExecutor'):
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(doWork) for _ in range(10)]

# threaded function
def _countEvens(start, end):
    # count even numbers in a range
    count = sum(1 for number in range(start, end) if number % 2 == 0)
    return count

def _parallelCount(executorType, endNumber, totalWorkers):
    # determine the range for each thread
    step = endNumber // totalWorkers
    futures = []

    before = time.monotonic()
    with executorType(max_workers=totalWorkers) as executor:
        # submit tasks to the thread pool
        for i in range(totalWorkers):
            start = i * step
            end = (i + 1) * step - 1
            if i == totalWorkers - 1:
                end = endNumber # last iteration, stop at end
                
            # execute each task
            futures.append(executor.submit(_countEvens, start, end))

        # collect results as they are completed using result()
        totalCount = sum(f.result() for f in concurrent.futures.as_completed(futures))

    duration = time.monotonic() - before
    assert(totalCount == endNumber / 2)
    return duration

def countEvens():
    # define the range to count evens
    endNumber = 10000000
    totalWorkers = 8

    before = time.monotonic()
    _countEvens(0, endNumber)
    singleThreadedDuration = time.monotonic() - before
    multithreadedDuration = _parallelCount(concurrent.futures.ThreadPoolExecutor, endNumber, totalWorkers)
    multiProcessDuration = _parallelCount(concurrent.futures.ProcessPoolExecutor, endNumber, totalWorkers)
    # ^Note: ProcessPoolExecutor is the newer and preferred interface over multiprocessing.Pool

    print(f'\nSingle threaded: {singleThreadedDuration}')
    print(f'Multithreaded: {multithreadedDuration}')
    print(f'Multi-process: {multiProcessDuration}')
    
    '''Sample output:
    Single threaded: 0.672
      Multithreaded: 0.985
      Multi-process: 0.343
    '''

def main():
    threadPoolExecutor()
    processPoolExecutor()
    countEvens()

if __name__ == '__main__':
    main()
    print('Tests passed!')
