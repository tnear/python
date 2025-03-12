# errno — Standard errno system symbols
# https://docs.python.org/3/library/errno.html

import errno

def basic():
    assert errno.EIO == 5

def print_all_sorted():
    error_codes = [(name, getattr(errno, name)) for name in dir(errno)
                   if isinstance(getattr(errno, name), int)]

    # sort by the numeric value
    error_codes.sort(key=lambda x: x[1])

    for name, value in error_codes:
        print(f'{value}: {name}')

def main():
    basic()
    print_all_sorted()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
