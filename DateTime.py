'''
The datetime module supplies classes for manipulating dates and times.
https://docs.python.org/3/library/datetime.html
'''

import datetime
import time

# timedelta represents a duration
def timeDelta():
    # call constructor with time(s).
    # Multiple times such as timedelta(seconds=1, hours=2, days=3) is also valid
    delta = datetime.timedelta(milliseconds=0.1)

    # sleep for 0.1 milliseconds (0.0001 seconds).
    assert delta.seconds == 0 # note: seconds an integer, so cannot use it
    assert delta.total_seconds() == 0.0001
    time.sleep(delta.total_seconds())

    # there is no milliseconds field, so verify that 0.1 ms equals 100 microseconds
    assert delta.microseconds == 100
    assert delta.seconds == 0
    assert delta.days == 0
    # documented way to get milliseconds:
    millis = delta / datetime.timedelta(milliseconds=1)
    assert millis == 0.1

    # add two seconds. This simply does a += on the seconds
    # field and leaves microseconds unchanged.
    delta += datetime.timedelta(seconds=2)
    assert delta.seconds == 2
    assert delta.microseconds == 100

    # keep subtracting 100 milliseconds until time drops to zero
    numIter = 0
    subtract = datetime.timedelta(milliseconds=100)
    # compare to datetime.timedelta() which creates a duration of 0
    while delta > datetime.timedelta():
        delta -= subtract
        numIter += 1

    assert numIter == 21

def timeDeltaNegative():
    # there are 86400 seconds in a day. If you
    # pass in a negative value, it subtracts it
    # from the max (mod max).
    delta = datetime.timedelta(seconds=-1)
    assert delta.seconds == 86_400 - 1

    # mod example
    delta = datetime.timedelta(seconds=(86400*2) - 2)
    assert delta.seconds == 86_400 - 2

def now():
    current_timestamp = datetime.datetime.now()
    # example now() output:
    # current_timestamp=datetime.datetime(2025, 6, 9, 15, 35, 45, 219770)
    print(f'{current_timestamp=}')

def main():
    timeDelta()
    timeDeltaNegative()
    now()

if __name__ == '__main__':
    main()
    print('Tests passed!')
