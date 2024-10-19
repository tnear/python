# weakref — Weak references
# https://docs.python.org/3/library/weakref.html

import weakref
import sys

class C:
    def __init__(self):
        print('obj being created')

    def __del__(self):
        print('obj being destroyed')

def weakRef():
    c = C()
    del c # calls __del__

    c = C()
    assert sys.getrefcount(c) == 2

    # create weak reference to c
    # weak references do not increment ref count
    d = weakref.ref(c)
    assert sys.getrefcount(c) == 2

    # 'call' the weakref using ()
    assert d() == c

    # delete what weakref refers to (c) and verify the reference is now none
    del c
    assert d() is None

def main():
    weakRef()

if __name__ == '__main__':
    main()
    print('Tests passed!')
