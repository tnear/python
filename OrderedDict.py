# Dictionary subclass which preserves key order
# https://docs.python.org/3/library/collections.html

import collections

def f():
    od = collections.OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    od['d'] = 4

    assert list(od.keys()) == ['a', 'b', 'c', 'd']
    assert list(od.values()) == [1, 2, 3, 4]

    # remove a, b
    od.pop('b')
    od.pop('a')
    assert list(od.keys()) == ['c', 'd']

    # add a to end
    od['a'] = 1
    assert list(od.keys()) == ['c', 'd', 'a']

def main():
    f()

if __name__ == '__main__':
    main()
    print('Tests passed!')
