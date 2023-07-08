import math
import re

def printExample():
    # assign and return value in same expression
    # prints True
    print(walrus := True)

def assignmentExpressions():
    # aka 'Walrus Operator', :=

    # Computes math.cos(2) multiple times
    result = [math.cos(2), math.cos(2)**2, math.cos(2)**2]

    # Computes math.cos(2) once using :=
    result = [x := math.cos(2), x**2, x**3]
    print(result)

# https://martinheinz.dev/blog/79
def regex():
    test = 'Something to match'
    pattern1 = r'^.*(thing).*'
    pattern2 = r'^.*(not present).*'

    m = re.match(pattern1, test)
    if m:
        print('Matched 1st pattern: ' + m.group(1))
    else:
        m = re.match(pattern2, test)
        if m:
            print('Matched 2nd pattern: ' + m.group(1))

    # Cleaner using :=
    if m := re.match(pattern1, test):
        print('Matched 1st pattern: ' + m.group(1))
    elif m := re.match(pattern2, test):
        print('Matched 2nd pattern: ' + m.group(1))

def main():
    printExample()
    assignmentExpressions()
    regex()

if __name__ == '__main__':
    main()
    print('Tests passed!')
