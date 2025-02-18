import math

def string():
    assert str(3) == '3'
    assert "module 'math'" in str(math)
    assert str(math.pi) == '3.141592653589793'

def floatingPoint():
    assert float('1.234') == 1.234

def main():
    string()
    floatingPoint()

if __name__ == '__main__':
    main()
    print('Tests passed!')
