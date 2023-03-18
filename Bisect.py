# Find or insert into sorted container
# bisect — Array bisection algorithm
# https://docs.python.org/3/library/bisect.html

import bisect

# bisect() is O(lg N) because list must be sorted
def bisectFcn():
    li = [1, 3, 4, 4, 4, 6, 7]
    assert li == sorted(li)

    numToLookFor = 4
    # default low idx = 0, default high index = len(container)
    idx = bisect.bisect(li, numToLookFor)
    assert idx == 5

    startIdx = 0
    stopIdx = 3
    idx = bisect.bisect(li, numToLookFor, startIdx, stopIdx)
    assert idx == 3

# insort() is O(N) because it calls insert() which is O(N)
def insort():
    # insort() inserts into sorted list
    li = [1, 3, 4, 4, 4, 6, 7]
    assert li == sorted(li)

    numToInsert = 5
    bisect.insort(li, numToInsert)
    assert li == [1, 3, 4, 4, 4, 5, 6, 7]

def main():
    bisectFcn()
    insort()

if __name__ == '__main__':
    main()
    print('Tests passed!')
