# https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/
# A decorator is a function that takes a function as its only parameter and returns a function.

import functools
import time

# Decorator function:
def decorate_message(func):
    # Nested function
    def addWelcome(site_name):
        return 'Welcome to ' + func(site_name)
 
    # Decorator returns a function
    return addWelcome

# Decorator function usage: 
@decorate_message
def site(siteName):
    return siteName

def printDecorator():
    # Prints: 'Welcome to Python!
    # Note: without @decorate_message, it just prints 'Python!'
    print(site('Python!'))

def beforeAfterDecorator(func):
    def wrapper():
        print('Before func')
        func()
        print('After func')
    return wrapper

@beforeAfterDecorator
def printLine():
    print('My line')

def printDecorator2():
    printLine()
    '''
    prints:
    Before func
    My line
    After func
    '''

# *args and **kwargs are needed for functions which accept arguments
def doTwice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@doTwice
def printLine2(value):
    # the doTwice decorator causes this to be called twice
    print(f'This appears twice: {value}')

def timer(func):
    # Print the runtime of the decorated function
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f'Finished {func.__name__} in {run_time:.4f} seconds')
        return value
    return wrapper_timer

@timer
def timeSum(numTimes):
    # prints:
    # Finished 'timeSum' in 0.0213 secs
    for _ in range(numTimes):
        sum([i**2 for i in range(10000)])

def runTimer():
    timeSum(5)

def main():
    printDecorator()
    printDecorator2()
    printLine2('My Value')
    runTimer()

if __name__ == '__main__':
    main()
    print('Tests passed!')
