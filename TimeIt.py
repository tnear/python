# timeit — Measure execution time of small code snippets
# https://docs.python.org/3/library/timeit.html

import timeit

def time():
    # default number is 1,000,000
    duration = timeit.timeit('output = 2 ** 128')
    assert duration < 0.5

    # specify a smaller number
    duration = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    assert duration < 0.5

def setup():
    setup = 'import random'
    stmt = '''
def test():
    return random.randint(10, 100)
'''

    duration = timeit.timeit(stmt=stmt, setup=setup)
    assert duration < 0.5

def testRange():
    L = [i for i in range(1000)]

# use setup to import the function to be tested (testRange)
def moduleAccess():
    duration = timeit.timeit('testRange()', setup='from __main__ import testRange', number=1000)
    assert duration < 0.5

def pow1024(x):
    return x ** 1024

def pow2048(x):
    return x ** 2048

# use globals() to provide access to everything in global namespace
def globalAccess():
    duration = timeit.timeit('[func(101) for func in (pow1024, pow2048)]', globals=globals(), number=1000)
    assert duration < 0.5

def main():
    time()
    setup()
    moduleAccess()
    globalAccess()

if __name__ == '__main__':
    main()
    print('Tests passed!')
