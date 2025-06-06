# https://www.geeksforgeeks.org/with-statement-in-python

# Classes must define __enter__ and __exit__ to support the 'with' statement.
import pathlib

class MessageWriter:
    def __init__(self, fileName):
        self.fileName = fileName
        self.file_handle = None

    # __enter__ is called automatically when using the 'with' statement
    def __enter__(self):
        # acquire file resource
        print('__enter__')
        self.file_handle = open(self.fileName, 'w', encoding='utf-8')
        return self.file_handle

    # __exit__ is called automatically when 'with' scope is exited
    def __exit__(self, *args):
        # free file resource
        print('__exit__')
        self.file_handle.close()
        pathlib.Path(self.file_handle.name).unlink()

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

# a class which must be used inside a 'with' statement
class WithOnlyClass:
    def __init__(self):
        self._entered = False

    def __enter__(self):
        self._entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def some_method(self):
        if not self._entered:
            raise RuntimeError("This class can only be used within a 'with' statement")

def with_only_class():
    with WithOnlyClass() as obj:
        obj.some_method()  # permitted

    # prevent usages outside of 'with'
    obj2 = WithOnlyClass()
    try:
        obj2.some_method()
        assert False  # unreachable
    except RuntimeError:
        print('caught error')

def main():
    withClass()
    nested()
    with_only_class()

if __name__ == '__main__':
    main()
    print('Tests passed!')
