# Z3 Theorem Prover
# https://github.com/Z3Prover/z3

import z3

def integer():
    x = z3.Int('x')
    y = z3.Int('y')

    z3.solve(x > 2, y < 10, x + 2*y == 7)
    # prints:
    # [y = 0, x = 7]

def ints():
    x, y = z3.Ints('x y') # syntax for creating multiple integers
    z3.solve(x > 4, y > 3, x - x * y**2 <= 12)
    # prints: [x = 5, y = 4]

def real():
    x = z3.Real('x')
    y = z3.Real('y')
    z = x + y >= 3
    assert z.num_args() == 2

def bool():
    # boolean logic
    a, b, c = z3.Bools('a b c')
    z3.solve(z3.And(a, b), z3.Or(b, c))
    # prints: [b = True, a = True, c = False]

def main():
    integer()
    ints()
    real()
    bool()

if __name__ == '__main__':
    main()
    print('Tests passed!')
