import os

def fileBasics():
    file = 'a.txt'
    assert not os.path.exists(file)

    # create file for writing (w)
    # 'a' (not shown) = append
    f = open(file, 'w')

    # write
    f.write('hello world!')
    f.close()
    assert os.path.exists(file)

    # open file for reading (r)
    f = open(file, 'r')
    data = f.read()
    assert data == 'hello world!'
    f.close()

    # delete file when done
    os.remove(file)
    assert not os.path.exists(file)

def readBytes():
    file = 'b.txt'
    f = open(file, 'w')
    f.write('abcdefg')
    f.close()

    with open(file) as f:
        assert f.read(1) == 'a'  # reads 'a'
        assert f.read(2) == 'bc'  # reads 'bc'
        assert f.read(1) == 'd' # reads 'd'
        # -1 index is default and reads rest of file
        assert f.read(-1) == 'efg' # reads 'efg'

    os.remove(file)

def readlines():
    file = 'c.txt'
    f = open(file, 'w')
    f.write('hello\nworld!')
    f.close()

    txt = ''
    with open(file) as f:
        for line in f.readlines():
            txt += line

    assert txt == 'hello\nworld!'
    os.remove(file)

def main():
    fileBasics()
    readBytes()
    readlines()

if __name__ == '__main__':
    main()
    print('Tests passed!')
