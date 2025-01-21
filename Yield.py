# Yield suspends a function's execution and saves state to
# allow resuming execution later.

import types

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

def _generate_numbers(n):
    # return one incrementing number at a time
    yield from range(n)

    # equivalent syntax as yield from:
    #for i in range(n):
    #    yield i

def generator_object():
    gen_obj = _generate_numbers(3)
    assert isinstance(gen_obj, types.GeneratorType)

    nums = []
    for num in gen_obj:
        nums.append(num)
    assert nums == [0, 1, 2]

def _accumulator():
    total = 0
    while True:
        # yield pauses generator function and returns 'total'.
        # The next time the generator is called, it assigns the
        # value received using <generator>.send(value).
        value = yield total
        total += value

# yield assignment is often used for two-way communication
# with the caller and receiver.
def assignment():
    acc = _accumulator()
    assert isinstance(acc, types.GeneratorType)
    # start generator using next() which advances to yield statement
    result = next(acc)
    assert result == 0

    # send value of 10
    result = acc.send(10)
    assert result == 10

    # send 20. This takes 10 + 20 to return 30
    result = acc.send(20)
    assert result == 30

def main():
    Yield()
    Yield2()
    generator_object()
    assignment()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
