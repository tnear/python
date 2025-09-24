'''
Python built-in functions
https://docs.python.org/3/library/functions.html
'''

def int_fcn():
    # default base is 10
    assert 13 == int(13)
    # int() truncates
    assert 3 == int(3.9)
    # string supported
    assert 4 == int('4')

    # binary
    assert 6 == int('110', base=2)

    # hex
    assert 255 == int('ff', base=16)

    # base 0 determines the base from its prefix
    # hex (0x)
    assert 255 == int('0xff', base=0)
    # binary (0b)
    assert 6 == int('0b110', base=0)
    # base 10 (no prefix)
    assert 25 == int('25', base=0)

# eval() should only be called on trusted code
# see ast.literal_eval for a preferred approach
def eval_fcn():
    x = 1
    assert 2 == eval('x+1')

def main():
    int_fcn()
    eval_fcn()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
