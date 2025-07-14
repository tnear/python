# File and Directory Access
# https://docs.python.org/3/library/filesys.html

import os

def fileWith():
    # Use 'with' keyword to close file automatically
    file = 'a.txt'

    # write file. write() returns number of bytes written
    with open(file, 'w', encoding='utf-8') as f:
        num_bytes = f.write('hello world!')

    assert num_bytes == 12

    # read entire file
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()

    assert data == 'hello world!'
    os.remove(file)

def fileHandle():
    file = 'a.txt'
    assert not os.path.exists(file)

    # create file for writing (w)
    # 'a' (not shown) = append
    f = open(file, 'w', encoding='utf-8')

    # write
    f.write('hello world!')
    f.close()
    assert os.path.exists(file)

    # open file for reading (r)
    f = open(file, 'r', encoding='utf-8')
    data = f.read()
    assert data == 'hello world!'
    f.close()

    # delete file when done
    os.remove(file)
    assert not os.path.exists(file)

def readBytes():
    file = 'b.txt'
    f = open(file, 'w', encoding='utf-8')
    f.write('abcdefg')
    f.close()

    with open(file, encoding='utf-8') as f:
        assert f.read(1) == 'a'  # reads 'a'
        assert f.read(2) == 'bc'  # reads 'bc'
        assert f.read(1) == 'd' # reads 'd'
        # -1 index is default and reads rest of file
        assert f.read(-1) == 'efg' # reads 'efg'

    os.remove(file)

def readlines():
    file = 'c.txt'
    f = open(file, 'w', encoding='utf-8')
    f.write('hello\nworld!')
    f.close()

    txt = ''
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            txt += line

    assert txt == 'hello\nworld!'
    os.remove(file)

def create():
    # Create file using 'with' keyword
    # which does not requiring close
    file = 'a.txt'
    with open(file, 'w', encoding='utf-8') as f:
        f.write('hello')

    assert os.path.exists(file)
    os.remove(file)
    assert not os.path.exists(file)

def fileno():
    # use fileno() method to get file descriptor
    file = 'fileno.txt'
    with open(file, 'w', encoding='utf-8') as f:
        assert f.fileno() > 0

    os.remove(file)

def main():
    fileWith()
    fileHandle()
    readBytes()
    readlines()
    create()
    fileno()

if __name__ == '__main__':
    main()
    print('Tests passed!')
