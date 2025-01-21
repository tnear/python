'''
types — Dynamic type creation and names for built-in types
https://docs.python.org/3/library/types.html
'''

import types

def generate_numbers():
    yield from range(3)

def generator_type():
    gen = generate_numbers()
    assert isinstance(gen, types.GeneratorType)

def main():
    generator_type()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
