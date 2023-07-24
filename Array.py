# array — Efficient arrays of numeric values
# https://docs.python.org/3/library/array.html

# Every element must be same data type (like NumPy and unlike list, tuple, etc.)

import array

def append():
    # append with array works same as lists
    intTypeCode = 'i'
    arrayOfInt = array.array(intTypeCode, [3, 4, 5])
    assert isinstance(arrayOfInt[0], int)
    assert arrayOfInt.itemsize == 4

    assert arrayOfInt[0] == 3
    assert arrayOfInt[1] == 4
    assert arrayOfInt[2] == 5

    # append new value to end
    arrayOfInt.append(6)
    assert arrayOfInt[-1] == 6

def typeCodes():
    # all C data types have a type code
    doubleCode = 'd'
    arrayOfDouble = array.array(doubleCode, [3, 4, 5])
    assert isinstance(arrayOfDouble[0], float)
    assert arrayOfDouble.itemsize == 8

def tolist():
    # convert array to list
    arr = array.array('i', [3, 4, 5])
    arrList = arr.tolist()
    assert arrList == [3, 4, 5]

def main():
    append()
    typeCodes()
    tolist()

if __name__ == '__main__':
    main()
    print('Tests passed!')
