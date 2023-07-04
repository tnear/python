# UserDict.py
# A wrapper around dictionary which allows more customization
# https://docs.python.org/3/library/collections.html

import collections

# Inherit from UserDict
class MyDict(collections.UserDict):

    # Disallow pop() and popitem()
    def pop(self, s = None):
        raise RuntimeError('Pop not allowed')

    def popitem(self, s = None):
        raise RuntimeError('Popitem now allowed')

def f():
    d = MyDict({'a': 1, 'b': 2, 'c': 3})
    print(d)

    # Verify errors
    try:
        assert len(d) == 3
        d['d'] = 4
        assert len(d) == 4
        d.pop()
        assert False
    except RuntimeError:
        # pop() should throw RuntimeError
        pass
    else:
        assert False

    try:
        d.popitem(1)
        assert False
    except RuntimeError:
        # popitem() should throw RuntimeError
        pass
    else:
        assert False

def main():
    f()

if __name__ == '__main__':
    main()
    print('Tests passed!')
