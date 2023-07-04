# ChainMap.py
# Allows managing multiple dictionaries with one interface
# ChainMap does not combine dictionaries (allows multiple keys)
# https://docs.python.org/3/library/collections.html

import collections

def f():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 2.5, 'c': 3}

    cm = collections.ChainMap(d1, d2)
    keys = list(cm.keys())
    assert keys == ['b', 'c', 'a']

    assert cm['b'] == 2

    # index into 2nd (index=1) dictionary
    assert cm.maps[1]['b'] == 2.5 # is there a better way to access 2.5?

def main():
    f()

if __name__ == '__main__':
    main()
    print('Tests passed!')
