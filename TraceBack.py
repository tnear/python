# traceback — Print or retrieve a stack traceback (backtrace)
# https://docs.python.org/3/library/traceback.html

import traceback

def print_stack():
    # prints call stack (returns nothing)
    print('print_stack')
    traceback.print_stack()

# print_exc prints full traceback of most recently raised exception
def print_exc():
    # induce exception
    a = [1, 2, 4]
    caught = False
    try:
        print(a[500])
    except IndexError:
        caught = True
        print('print_exc')
        traceback.print_exc()

    assert caught

# format_exc is like print_exc, but returns a string
def format_exc():
    # induce exception
    a = [1, 2, 4]
    caught = False
    try:
        print(a[500])
    except IndexError:
        caught = True
        print('format_exc')
        res = traceback.format_exc()
        print(f'{res=}')

    assert caught

def main():
    print_stack()
    print_exc()
    format_exc()

if __name__ == '__main__':
    main()
    print('Tests passed!')
