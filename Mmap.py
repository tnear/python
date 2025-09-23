'''
Memory-mapped file support
https://docs.python.org/3/library/mmap.html
https://realpython.com/python-mmap/
'''

import mmap
import ctypes
import pathlib
import timeit

def basic_usage():
    # write file (no mmap)
    file = 'a.txt'
    with open(file, 'w', encoding='utf-8') as f:
        f.write('hello world!')

    # use mmap to read the entire file into memory
    # fileno(): returns file descriptor
    # length: length of bytes in map. 0 is special and means create map large enough for entire file
    # ACCESS_READ: tells that the mmap file will be read (not written)
    with open(file, mode='r', encoding='utf8') as fileObj:
        with mmap.mmap(fileObj.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObj:
            text = mmapObj.read()
            assert text == b'hello world!'

    pathlib.Path(file).unlink()

def regular_io(filename):
    with open(filename, mode='r', encoding='utf8') as file_obj:
        text = file_obj.read()

def mmap_io(filename):
    with open(filename, mode='r', encoding='utf8') as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()

def benchmark():
    # write bytes
    file = 'a.txt'
    with open(file, 'w', encoding='utf-8') as f:
        f.write('hello world! ' * 1000000)

    regularDuration = timeit.timeit('regular_io("a.txt")', number=5, globals=globals())
    print(regularDuration)

    mmapDuration = timeit.timeit('mmap_io("a.txt")', number=5, globals=globals())
    print(mmapDuration)

    # cleanup
    pathlib.Path(file).unlink()

def anonymous_memory():
    # use -1 fileno to indicate anonymous memory
    with mmap.mmap(-1, 8) as mm:
        # get memory address
        mem_addr = ctypes.addressof(ctypes.c_char.from_buffer(mm))
        assert mem_addr > 0

def main():
    basic_usage()
    benchmark()
    anonymous_memory()

if __name__ == '__main__':
    main()
    print('Tests passed!')
