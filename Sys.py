import math
import os
import sys

def version():
    assert '3.' in sys.version

def stdout():
    sys.stdout.write('hello world!\n')

def path():
    pathLower = [x.lower() for x in sys.path]
    assert os.getcwd().lower() in pathLower

def getrefcount():
    a = [1, 2, 3]
    assert sys.getrefcount(a) > 1
    assert sys.getrefcount(1) > 100

def maxsize():
    assert sys.maxsize == 2 ** 63 - 1
    assert math.log2(sys.maxsize) == 63.0

def main():
    version()
    stdout()
    path()
    getrefcount()
    maxsize()

if __name__ == '__main__':
    main()
    print('Tests passed!')
