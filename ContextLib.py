# contextlib — Utilities for with-statement contexts
# https://docs.python.org/3/library/contextlib.html

import contextlib
import pathlib

# contextmanager is an alternative option to creating a
# class and implementing the __enter__ and __exit__
# methods. contextmanager is used the 'with' keyword
@contextlib.contextmanager
def contextManager(fname):
    print('Entering implicit __enter__ block...')
    myFile = open(fname, 'w')

    # yield resource to be used within WITH block
    yield myFile

    print('Entering implicit __exit__  block...')
    myFile.close()
    pathlib.Path(myFile.name).unlink()

def testContextManager():
    '''
    Prints:
    Entering implicit __enter__ block...
    Inside with WITH block
    Entering implicit __exit__  block...
    '''
    with contextManager('MyFile.txt') as _:
        print('Inside with WITH block')

def main():
    testContextManager()

if __name__ == '__main__':
    main()
    print('Tests passed!')
