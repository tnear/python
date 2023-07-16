# Lambda functions are Python's syntax for short, anonymous function

def basic():
    # syntax:
    # fcn = lambda <args> : <expr>
    fcn = lambda a, b : a * b
    assert fcn(2, 5) == 10
    assert fcn([2], 5) == [2, 2, 2, 2, 2]
    assert fcn(1j, 4) == 4j
    assert fcn('a', 3) == 'aaa'

def zeroArgs():
    fcn = lambda : 'abc'
    assert fcn() == 'abc'

def ternary():
    myMax = lambda a, b : a if (a > b) else b
    assert myMax(2, 3) == 3
    assert myMax(2, -3) == 2
    assert myMax(-3, -3) == -3

def filterFcn():
    # get odd numbers using 'filter'
    result = filter(lambda x : x % 2, [1, 2, 3, 4, 5])
    assert list(result) == [1, 3, 5]

def main():
    basic()
    zeroArgs()
    ternary()
    filterFcn()

if __name__ == '__main__':
    main()
    print('Tests passed!')
