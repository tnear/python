# copy — Shallow and deep copy operations
# https://docs.python.org/3/library/copy.html

import copy

def shallowCopy():
    # starting array, note the nested structure
    array = [1, 2, [3, 4], 5]

    # shallow copy does not copy nested objects
    shallow = copy.copy(array)

    # prove this by changing 3 -> 6
    shallow[2][0] = 6

    # show that the array and shallow copy are the same
    assert array[2][0] == shallow[2][0]
    assert array == [1, 2, [6, 4], 5]

def deepCopy():
    # same starting array as shallowCopy()
    array = [1, 2, [3, 4], 5]

    # make deep copy
    deep = copy.deepcopy(array)

    # change the nested element
    deep[2][0] = 6

    # verify that array and deep remain different
    assert array[2][0] != deep[2][0]
    assert array == [1, 2, [3, 4], 5]
    assert deep  == [1, 2, [6, 4], 5]

def main():
    shallowCopy()
    deepCopy()

if __name__ == '__main__':
    main()
    print('Tests passed!')
