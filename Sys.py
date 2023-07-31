# sys — System-specific parameters and functions
# https://docs.python.org/3/library/sys.html

import math
import os
import sys

def version():
    # get Python version
    assert '3.' in sys.version

def executable():
    # get python executable location
    assert 'python.' in sys.executable

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

def getsizeof():
    a = [1, 2, 3, 4, 5]
    assert sys.getsizeof(a) == 96

    # tuples are more compact than lists
    b = tuple(a)
    assert sys.getsizeof(b) == 80

def byteorder():
    assert sys.byteorder == 'little'

# Contains directory where Python files are installed
# Note: this value changes for virtual environments (venv)
def prefix():
    assert 'Python' in sys.prefix
    inVEnv = sys.prefix != sys.base_prefix

# base_prefix does not change even in virtual environments
def basePrefix():
    assert 'Python' in sys.base_prefix

def main():
    version()
    executable()
    stdout()
    path()
    getrefcount()
    maxsize()
    getsizeof()
    byteorder()
    prefix()
    basePrefix()

if __name__ == '__main__':
    main()
    print('Tests passed!')
