# heapq — Heap queue algorithm
# https://docs.python.org/3/library/heapq.html

import heapq
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

def heappush():
    # heappush(list, newElement)
    li = []
    heapq.heappush(li, 3)
    heapq.heappush(li, 1)
    heapq.heappush(li, 4)
    heapq.heappush(li, 5)
    heapq.heappush(li, 2)

    # Min-heap
    # Removes lowest element in heap
    assert heapq.heappop(li) == 1
    assert heapq.heappop(li) == 2
    assert heapq.heappop(li) == 3
    assert heapq.heappop(li) == 4
    assert heapq.heappop(li) == 5

def heapify():
    # Convert to heap order
    li = [5, 7, 9, 1, 3]

    heapq.heapify(li)
    assert li == [1, 3, 9, 7, 5]

def nsmallest():
    # Returns smallest numbers in heap without altering it
    li = [6, 4, 3, 5, 2, 1]

    largest = heapq.nsmallest(3, li)
    assert largest == [1, 2, 3]

def main():
    heappush()
    heapify()
    nsmallest()

if __name__ == '__main__':
    main()
    print('Tests passed!')
