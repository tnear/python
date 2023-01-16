import math
import sys

def separator():
    # default separator is space

    # outputs 'a b c'
    print('a', 'b', 'c')

    # outputs 'a-b-c'
    print('a', 'b', 'c', sep='-')

def end():
    # default end char is '\n'

    # outputs 'abc\n'
    print('abc')

    # outputs 'abc' (no newline)
    print('abc', end='')

def fmt():
    # output 5 digits of pi
    print('pi: %.5f' % math.pi)
    # pi: 3.14159

    # '%d' = int
    # substitute first %d with 2 and 2nd with 4
    print('1: %d, 3: %d' % (2, 4))
    # outputs '1: 2, 3: 4'

def escape():
    # how to output '?' char in formatted string:
    print('10%d%%' % 1)
    # outputs: '101%'
    # "%d = integer
    # % (x2) = '%' char in format mode"

def stderr():
    print('My stdout', file=sys.stdout) # default is sys.stdout
    print('My stderr', file=sys.stderr)

def main():
    separator()
    end()
    fmt()
    escape()
    stderr()

if __name__ == '__main__':
    main()
    print('Tests passed!')
