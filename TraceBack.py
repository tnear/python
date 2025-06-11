# traceback — Print or retrieve a stack traceback (backtrace)
# https://docs.python.org/3/library/traceback.html

import traceback

def get_call_stack():
    # prints call stack (returns nothing)
    traceback.print_stack()

def main():
    get_call_stack()

if __name__ == '__main__':
    main()
    print('Tests passed!')
