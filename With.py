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

def main():
    withClass()

if __name__ == '__main__':
    main()
    print('Tests passed!')
