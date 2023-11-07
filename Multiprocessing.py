# multiprocessing — Process-based parallelism
# https://docs.python.org/3/library/multiprocessing.html
# multiprocessing spawns processes, which avoids encountering
# the global interpreter lock (GIL). multiprocessing often
# outperforms threading for CPU-bound tasks.
# multiprocessing leverages multiple processors on a machine.

# See also: ConcurrentFutures.py

import multiprocessing

def cpuCount():
    numCpu = multiprocessing.cpu_count()
    print(f'Number of CPU: {numCpu}')

def _calculateSquare(num: int, results, idx):
    results[idx] = num * num

def _returnSquare(num: int):
    return num * num

def process():
    # the Process class creates another Python process
    # arguments must be passed via the args parameter

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # create a list to keep track of processes
    processes = []

    # create a multiprocessing array to hold the results
    # this requires a separate data structure b/c these are new processes, not threads
    # i = integer (signed)
    results = multiprocessing.Array('i', len(numbers))

    # create a process for each number
    for i, number in enumerate(numbers):
        process = multiprocessing.Process(target=_calculateSquare, args=(number, results, i))
        processes.append(process)
        process.start()

    # wait for all processes to finish execution
    for process in processes:
        process.join()

    expResult = [number * number for number in numbers]
    assert isinstance(results, multiprocessing.sharedctypes.SynchronizedArray)
    assert(results[:] == expResult)

def pool():
    numbers = [1, 2, 3, 4]

    # pool uses a context manager to create and destruct the pool
    # Note: ProcessPoolExecutor is the newer and preferred interface over multiprocessing.Pool
    with multiprocessing.Pool(processes=4) as pool:
        # map() blocks until the result is ready
        squares = pool.map(_returnSquare, numbers)

    exp = [number * number for number in numbers]
    assert(exp == squares)

def _producer(queue):
    # produce some data and put it on the queue
    for i in range(5):
        print(f'Putting item {i} on the queue')
        queue.put(i)

def _consumer(queue):
    # Consume data from the queue
    while True:
        item = queue.get()
        if item is None:
            # None signals the end
            break
        print(f'Getting item {item} from the queue')
    print('Consumer finished')

def queue():
    # multiprocessing.Queue shares data between processes
    # mp.Queue is thread and process safe
    queue = multiprocessing.Queue()

    # start the producer process
    producerProcess = multiprocessing.Process(target=_producer, args=(queue,))
    producerProcess.start()

    # start the consumer process
    consumerProcess = multiprocessing.Process(target=_consumer, args=(queue,))
    consumerProcess.start()

    # wait for the producer to finish
    producerProcess.join()

    # put None on the queue to signal the consumer to end
    queue.put(None)

    # wait for the consumer to finish
    consumerProcess.join()
    assert queue.empty()

def main():
    cpuCount()
    process()
    pool()
    queue()

if __name__ == '__main__':
    main()
    print('Tests passed!')
