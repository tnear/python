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
    print(old)
    print(time.monotonic())
    assert time.monotonic() - old >= .05

def main():
    epoch()
    currentTime()
    intToString()
    duration()
    monotonic()

if __name__ == '__main__':
    main()
    print('Tests passed!')
