# Find or insert into sorted container
# bisect — Array bisection algorithm
# https://docs.python.org/3/library/bisect.html

import bisect

# bisect() returns the last insertion point to maintain sorted order
# bisect() is O(lg N) because list must be sorted
def bisectFcn():
    li = [1, 3, 4, 4, 4, 6, 7]
    #     0  1  2  3  4  5  6
    assert li == sorted(li)

    numToLookFor = 4
    # default low idx = 0, default high index = len(container)
    idx = bisect.bisect(li, numToLookFor)
    assert idx == 5

    startIdx = 0
    stopIdx = 3
    idx = bisect.bisect(li, numToLookFor, startIdx, stopIdx)
    assert idx == 3

# bisect_left() returns the first insertion point which maintains sorted order
def bisectLeft():
    li = [1, 3, 4, 4, 4, 6, 7]
    #     0  1  2  3  4  5  6
    numToLookFor = 4
    idx = bisect.bisect_left(li, numToLookFor)
    assert idx == 2

# insort() inserts into sorted list
# insort() is O(N) because it calls insert() which is O(N)
def insort():
    li = [1, 3, 4, 4, 4, 6, 7]
    assert li == sorted(li)

    numToInsert = 5
    bisect.insort(li, numToInsert)
    assert li == [1, 3, 4, 4, 4, 5, 6, 7]

def main():
    bisectFcn()
    bisectLeft()
    insort()

if __name__ == '__main__':
    main()
    print('Tests passed!')
