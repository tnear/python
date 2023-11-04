# gc — Garbage Collector interface
# https://docs.python.org/3/library/gc.html

import gc

# Define a simple class to demonstrate the gc module
class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'{self.name} object is being deleted')

def collect():
    # Create a cycle: objA references objB and objB references objA
    objA = Demo('A')
    objB = Demo('B')
    objA.other = objB
    objB.other = objA

    # Without manually running garbage collection, these objects won't be deleted
    # because of their cyclic references, even if we delete our original references
    del objA
    del objB

    # two Demo objects before running gc.collect()
    numObjects = 0
    for obj in gc.get_objects():
        if isinstance(obj, Demo):
            numObjects += 1
    
    assert numObjects == 2

    # Manually run garbage collection
    gc.collect()

    # no Demo objects after running gc.collect()
    for obj in gc.get_objects():
        assert not isinstance(obj, Demo)

def disable():
    # Disable and then enable automatic garbage collection
    gc.disable()
    assert not gc.isenabled()

    gc.enable()
    assert gc.isenabled()

def main():
    collect()
    disable()

if __name__ == '__main__':
    main()
    print('Tests passed!')
