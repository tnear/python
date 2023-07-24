# contextlib — Utilities for with-statement contexts
# https://docs.python.org/3/library/contextlib.html

import contextlib
import pathlib

# contextmanager is an alternative option to creating a
# class and implementing the __enter__ and __exit__
# methods. contextmanager is used the 'with' keyword
@contextlib.contextmanager
def contextManager(fname):
    print('Entering implicit __enter__ block')
    myFile = open(fname, 'w')

    # yield resource to be used within WITH block
    yield myFile

    print('Entering implicit __exit__  block')
    myFile.close()
    pathlib.Path(myFile.name).unlink()

def testContextManager():
    '''
    Prints:
    Entering implicit __enter__ block
    Inside with WITH block
    Entering implicit __exit__  block
    '''
    with contextManager('MyFile.txt') as _:
        print('Inside with WITH block')

def testNested():
    # Note: contextlib.nested is deprecated
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    file3 = 'file3.txt'

    '''
    Instead of:
    with X as file1:
        with Y as file2:
            with Z as file3:

    , can use this syntax:
    '''
    with (
        open(file1, 'w') as f1,
        open(file2, 'w') as f2,
        open(file3, 'w') as f3
    ):
        f1.write('a')
        f2.write('b')
        f3.write('c')

    pathlib.Path(file1).unlink()
    pathlib.Path(file2).unlink()
    pathlib.Path(file3).unlink()

def main():
    testContextManager()
    testNested()

if __name__ == '__main__':
    main()
    print('Tests passed!')
