# ctypes - A foreign function library for Python
# https://docs.python.org/3/library/ctypes.html

import ctypes
import ctypes.util

# Load libc and call one if its functions.
# This can be useful when calling functions not available in python
# (but to keep it simple and portable, this example uses strlen)
def cdll():
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    test_string = b'hello, world!'

    # Always be explicit about data types. Without this, ctypes
    # converts everything to c_int, which can be dangerous
    libc.strlen.argtypes = [ctypes.c_char_p] # input is char*
    libc.strlen.restype = ctypes.c_size_t    # output arg is size_t

    # call libc strlen
    length = libc.strlen(test_string)
    assert length == len(test_string)

def main():
    cdll()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
