# inspect - Inspect live objects
# https://docs.python.org/3/library/inspect.html

import inspect

def current_frame():
    frame = inspect.currentframe()

    # get previous item on stack
    caller_frame = frame.f_back

    # get its class name via 'self' parameter
    caller_class = caller_frame.f_locals['self'].__class__.__name__
    assert caller_class == 'MyClass'
    
    # get calling method name
    caller_method = caller_frame.f_code.co_name
    assert caller_method == 'my_method'

class MyClass:
    def my_method(self):
        current_frame()

def main():
    c = MyClass()
    c.my_method()

if __name__ == '__main__':
    main()
    print('Tests passed!')
