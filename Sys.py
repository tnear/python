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
    assert 'python' in sys.executable

def stdout():
    sys.stdout.write('hello world!\n')

def path():
    pathLower = [x.lower() for x in sys.path]
    assert os.getcwd().lower() in pathLower

# python is a reference-counted language
def getrefcount():
    a = [1, 2, 3]
    # 1 for 'a', and 1 for ref count increment of using 'a' as a parameter
    assert sys.getrefcount(a) == 2

    # '1' is used in many places
    assert sys.getrefcount(1) > 100

def maxsize():
    assert sys.maxsize == 2 ** 63 - 1
    assert math.log2(sys.maxsize) == 63.0

def getsizeof():
    a = [1, 2, 3, 4, 5]
    assert sys.getsizeof(a) in (96, 104)

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

def int_max_str_digits():
    # default number of digits allowed for converting between
    # int and string
    assert sys.get_int_max_str_digits() == 4300

    # increase limit:
    # sys.set_int_max_str_digits(5000)
    # remove limit:
    # sys.set_int_max_str_digits(0)

def modules():
    # modules is a dictionary indicating which modules are loaded
    assert 'sys' in sys.modules

    # check if debug session is active
    debug_session = 'debugpy' in sys.modules
    print(f'{debug_session=}')

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
    int_max_str_digits()
    modules()

if __name__ == '__main__':
    main()
    print('Tests passed!')
