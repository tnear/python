# math — Mathematical functions
# https://docs.python.org/3/library/math.html

import math

def minMax():
    # Return 1st element alphabetically
    assert min(['zz', 'abc']) == 'abc'

    # Return shortest length
    assert min(['zz', 'abc'], key=len) == 'zz'

    # Return longest length
    assert max(['zz', 'abc'], key=len) == 'abc'

    # Default value
    assert max([], default = 1) == 1

def power():
    assert 2 ** 10 == 1024

    # 2 ^ 5 (mod 6)
    assert pow(2, 5, 6) == 2

    # math.pow converts to float
    assert math.pow(2, 5) == 32.0

def Complex():
    assert complex(3, 4) == 3 + 4j

def ulp():
    # similar to eps() in MATLAB
    assert math.ulp(0) == 5e-324
    assert math.ulp(2**53) == 2.0

def NaN():
    assert math.nan != math.nan

    # alt NaN syntax which does not need math import
    assert math.isnan(float('NaN'))

def nchoosek():
    assert math.comb(7, 3) == 35

def prod():
    assert math.prod([2, 3, 4]) == 24

def log():
    value = 2 ** 54
    assert math.log2(value) == 54

def custom_nchoosek():
    # binomial coefficient
    n = 4
    k = 3
    result = math.comb(n, k)
    assert result == 4

    result = math.comb(52, 3)
    assert result == 22100

def factorial():
    assert math.factorial(5) == 120
    assert math.factorial(25) == 15511210043330985984000000

# permutations = n! / (n - r)!
def permutations():
    assert math.perm(4, 0) == 1
    assert math.perm(4, 1) == 4
    assert math.perm(4, 2) == 12
    assert math.perm(4, 3) == 24
    assert math.perm(4, 4) == 24 # 0! = 1
    assert math.perm(52, 3) == 132600

def main():
    minMax()
    power()
    Complex()
    ulp()
    NaN()
    nchoosek()
    prod()
    log()
    custom_nchoosek()
    factorial()
    permutations()

if __name__ == '__main__':
    main()
    print('Tests passed!')