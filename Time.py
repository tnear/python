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
    # Get start time
    old = time.time()

    # Sleep .01 seconds
    seconds = .01
    time.sleep(seconds)

    # Measure elapsed time
    assert time.time() - old >= seconds

def main():
    epoch()
    currentTime()
    intToString()
    duration()

if __name__ == '__main__':
    main()
    print('Tests passed!')
