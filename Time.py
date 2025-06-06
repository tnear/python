# time — Time access and conversions
# https://docs.python.org/3/library/time.html

import time

def epoch():
    # 0 seconds after 1-1-70
    t = time.gmtime(0)
    assert t.tm_year == 1970

    # now
    t = time.gmtime(time.time())
    assert t.tm_year >= 2022

def currentTime():
    t = time.time()
    assert t > 1672074470.2505949

def intToString():
    string = time.ctime(1672074470.2505949)
    assert '2022' in string

def duration():
    # time.time() uses the system clock which is not monotonically increasing
    # time smearing and synchronization can cause time() to produce inaccurate results
    # Get start time
    old = time.time()

    # Sleep .01 seconds
    seconds = .01
    time.sleep(seconds)

    # Measure elapsed time (duration)
    assert time.time() - old >= seconds

def monotonic():
    # a monotonic clock only moves forward
    # it is a better choice for benchmarking
    old = time.monotonic()

    time.sleep(.1)
    print(f'{old=}')
    print(f'{time.monotonic()=}')
    assert time.monotonic() - old >= .05

def perf_counter():
    # perf_counter is used for high-resolution time measurements.
    # It returns a float.
    # It is not guaranteed to be monotonic
    start_time = time.perf_counter()

    time.sleep(0.001)
    end_time = time.perf_counter()
    perf_counter_time = end_time - start_time
    print(f'{perf_counter_time=}')

def main():
    epoch()
    currentTime()
    intToString()
    duration()
    monotonic()
    perf_counter()

if __name__ == '__main__':
    main()
    print('Tests passed!')
