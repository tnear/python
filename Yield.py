# Yield suspends a function's execution and saves state to
# allow resuming execution later.

def simpleGen():
    yield 1
    yield 2
    yield 3

def Yield():
    values = []
    for value in simpleGen():
        values.append(value)

    assert values == [1, 2, 3]

def nextSquare():
    i = 1
    # infinite loop where each iteration yields a square
    while True:
        yield i * i
        i += 1

# the __next__ method advances to next yield
def Yield2():
    n = nextSquare()
    assert n.__next__() == 1
    assert n.__next__() == 4
    assert n.__next__() == 9
    assert n.__next__() == 16

def main():
    Yield()
    Yield2()

if __name__ == '__main__':
    main()
    print('Tests passed!')
