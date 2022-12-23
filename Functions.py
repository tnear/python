# Miscellaneous information on Python functions

def arbitrary(*args):
    # *args creates a tuple of arguments
    for arg in args:
        print(arg, end=' ')

def namedArgs(a, b, c):
    print(a + b + c)

def keywordArgs(**kwargs):
    print('a: ' + kwargs['a'] + ', b: ' + kwargs['b'])

def argTypes(a: int, s: str) -> list:
    return [str(a) + s]

def idFcn():
    # id() returns unique constant for an object
    assert id(None) > 0

    val = id([])
    val2 = id([])
    assert val == val2

def hexFcn():
    # hex() converts integer to hex string
    assert hex(100) == '0x64'
    assert hex(101010101) == '0x6054ab5'

def inputFcn():
    #name = input('Enter your name: ')
    #print('Hello, ' + name)
    pass

def countFcn():
    # count number of values in a container

    # list
    assert [1, 2, 1, 4].count(1) == 2
    assert [1, 2, 1, 4].count(0) == 0

    # tuple
    assert (1, 3).count(3) == 1

def filterFcn():
    # get odd numbers using 'filter'
    result = filter(lambda x : x % 2, [1, 2, 3, 4, 5])
    assert list(result) == [1, 3, 5]

def main():
    arbitrary('a', 'b', 'c')
    namedArgs(a='1', b='2', c='3')
    keywordArgs(a='AA', b='BB')
    out = argTypes(1, 'a')
    assert out == ['1a']
    idFcn()
    hexFcn()
    inputFcn()
    countFcn()
    filterFcn()

if __name__ == '__main__':
    main()
    print('Tests passed!')
