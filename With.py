# https://www.geeksforgeeks.org/with-statement-in-python

# Classes must define __enter__ and __exit__ to support the 'with' statement.
import pathlib

class MessageWriter:
    def __init__(self, fileName):
        self.fileName = fileName

    # __enter__ is called automatically when using the 'with' statement
    def __enter__(self):
        # acquire file resource
        print('__enter__')
        self.file = open(self.fileName, 'w')
        return self.file

    # __exit__ is called automatically when 'with' scope is exited
    def __exit__(self, *args):
        # free file resource
        print('__exit__')
        self.file.close()
        pathlib.Path(self.file.name).unlink()

def withClass():
    with MessageWriter('myfile.txt') as mw:
        mw.write('hello world')

def nested():
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
        open(file1, 'w', encoding='utf-8') as f1,
        open(file2, 'w', encoding='utf-8') as f2,
        open(file3, 'w', encoding='utf-8') as f3
    ):
        f1.write('a')
        f2.write('b')
        f3.write('c')

    pathlib.Path(file1).unlink()
    pathlib.Path(file2).unlink()
    pathlib.Path(file3).unlink()

def main():
    withClass()
    nested()

if __name__ == '__main__':
    main()
    print('Tests passed!')
