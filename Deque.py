# Deque.py
# Double ended queue
# Allows efficient insert and pop at front and back

import collections

def append():
    d = collections.deque([2, 3, 4])
    d.append(5)
    d.appendleft(1)
    l = list(d)
    assert l == [1, 2, 3, 4, 5]

def pop():
    d = collections.deque([1, 2, 3, 4])
    d.pop()
    d.popleft()
    l = list(d)
    assert l == [2, 3]

def main():
    append()
    pop()

if __name__ == '__main__':
    main()
    print('Tests passed!')
