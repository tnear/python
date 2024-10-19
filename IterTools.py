# itertools — Functions creating iterators for efficient looping
# https://docs.python.org/3/library/itertools.html

import itertools
import operator

def accumulate():
    # first arg: iterable
    # 2nd arg: callback to execute (default operation is addition)

    # no callback (performs addition)
    nums = [2, 3, 5]
    result = list(itertools.accumulate(nums))
    assert result == [2, 5, 10]

    # product
    nums = [2, 3, 5]
    prod = list(itertools.accumulate(nums, operator.mul))
    assert prod == [2, 6, 30]

    # sum then subtract 10 using lambda function
    nums = [2, 3, 5]
    sub2 = list(itertools.accumulate(nums, lambda total, new : total + new - 10))
    assert sub2 == [2, -5, -10]

# count() makes an infinite iterator that returns evenly spaced values
def count():
    numbers = []
    for number in itertools.count(start=2, step=3):
        if number > 10:
            break
        numbers.append(number)

    assert numbers == [2, 5, 8]

# cycle() makes an infinite iterator returning elements from iterable
# and cycling back to beginning
def cycle():
    saved = []
    iterCount = 0
    for element in itertools.cycle('abc'):
        if iterCount >= 7:
            break
        else:
            iterCount += 1
            saved.append(element)

    assert saved == ['a', 'b', 'c', 'a', 'b', 'c', 'a']

# repeat() makes an iterator that returns the same object
# a specified number of times
def repeat():
    values = list(itertools.repeat(object=4, times=3))
    assert values == [4, 4, 4]

# returns all possible combinations (without replacement)
def combinations():
    values = list(itertools.combinations('ABC', 2))
    assert values == [('A', 'B'), ('A', 'C'), ('B', 'C')]

# takes a series of iterables and returns one long iterable
def chain():
    a = [1, 2, 3]
    b = ['d', 'e', 'f']
    c = [4.4, 5.5]

    result = list(itertools.chain(a, b, c))
    assert result == a + b + c

    # flatten 2D list
    matrix = [ [2, 3], [4, 5], [1, 2] ]
    result = list(itertools.chain(*matrix))
    assert result == [2, 3, 4, 5, 1, 2]

# similar to logical indexing in MATLAB
def compress():
    numbers = [2, 3, 4, 5]
    # create mask for even numbers
    mask = [True, False, True, False]

    result = list(itertools.compress(numbers, mask))
    assert result == [2, 4]

# makes an iterator that computes the function using arguments
def starmap():
    data = [(2, 6), (8, 4), (7, 3)]
    # multiply each of the individual tuples together
    # 2 * 6 = 12
    # 8 * 4 = 32, etc.
    result = list(itertools.starmap(operator.mul, data))
    assert result == [12, 32, 21]

def main():
    accumulate()
    count()
    cycle()
    repeat()
    combinations()
    chain()
    compress()
    starmap()

if __name__ == '__main__':
    main()
    print('Tests passed!')
