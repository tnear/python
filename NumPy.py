# NumPy.py
# NumPy arrays are stored contiguously, unlike Python lists.
# NumPy also is optimized for CPU architectures, making it faster
# https://www.w3schools.com/python/numpy/numpy_intro.asp

import numpy as np
import math

def arrayCreation():
    arr = np.array([2, 3, 1])
    assert np.array_equal(arr, [2, 3, 1])

def matrixCreation():
    m = np.matrix([[1, 1], [1, 0]])
    assert m.shape == (2, 2)
    assert m.ndim == 2

    # char syntax
    m = np.matrix('1 2; 3 4')
    assert np.all(m.flatten() == [1, 2, 3, 4])

def matrixIndexing():
    # [3 4
    #  5 6]
    m = np.matrix([[3, 4], [5, 6]])
    assert m[0, 0] == 3
    assert m[0, 1] == 4
    assert m[1, 0] == 5
    assert m[1, 1] == 6

    # use indexing to get 2nd column
    secondColumn = m[:, 1]
    assert np.array_equal(secondColumn, np.matrix([[4], [6]]))

    # equivalent syntax to above
    secondColumn = m[0:2, 1]
    assert np.array_equal(secondColumn, np.matrix([[4], [6]]))

def numel():
    m = np.matrix([[3, 4], [5, 6]])

    # size (NumPy) = numel (MATLAB)
    assert m.size == 4

def shape():
    # 3x2
    # [1, 2
    #  3, 4
    #  5, 6]
    m = np.matrix([[1, 2], [3, 4], [5, 6]])

    # shape (NumPy) = size (MATLAB)
    assert m.shape == (3, 2)

def all():
    arr = np.array([2, 4, 5, 6, 8])
    # method (returns scalar True):
    assert arr.all()
    # function:
    assert np.all(arr)

    # method:
    assert (arr >= 2).all()
    # function:
    assert np.all(arr >= 2)

    assert not np.all(arr % 2 == 1)

    arr = np.array([1, 0, 1])
    assert not arr.all()

def flatten():
    # similar to MATLAB's a(:)
    m = np.matrix('1 2; 3 4')
    assert np.all(m.flatten() == [1, 2, 3, 4])

    # alt syntax (prefer flatten())
    assert np.all(m.reshape(-1) == [1, 2, 3, 4])

def iterate():
    # 1D
    values = []
    a = np.array([1, 2, 3])

    for elem in a:
        values.append(elem)

    assert values == [1, 2, 3]

    values = []
    # 2D -- iterate over rows
    m = np.array([[1, 2], [3, 4]])
    for row in m:
        for elem in row:
            values.append(elem)

    assert values == [1, 2, 3, 4]

    values = []
    # 2D (nditer)
    m = np.mat('2 3; 4 5')
    for elem in np.nditer(m):
        values.append(elem)

    assert values == [2, 3, 4, 5]

def matrixMultiplication():
    m = np.mat('1 2; 3 4') * np.mat('2 3; 4 5')
    assert np.all(m == np.mat('10 13; 22 29'))

def arithmetic():
    assert math.pi == np.pi
    assert math.e == np.e

    arr = np.array([np.pi, np.e]) + 2
    assert arr[0] == np.pi + 2
    assert arr[1] == np.e + 2

    # Fibonacci
    arr = np.matrix([[1, 1], [1, 0]]) ** 8
    assert np.all(arr.flatten() == [34, 21, 21, 13])

def dataType():
    a = np.zeros([2,2], dtype=int)
    assert a.dtype == np.dtype('int32')
    assert isinstance(a, np.ndarray)
    assert isinstance(a[0], np.ndarray)
    assert isinstance(a[0][0], np.int32)

def logicalIndexing():
    a = np.array([1, 2, 3, 4, 5])
    assert np.array_equal(a > 3, [False, False, False, True, True])

    b = a[a > 3]
    assert np.array_equal(b, [4, 5])

    # multiple constraints
    c = a[(a >= 2) & (a % 2 == 1)]
    assert np.array_equal(c, [3, 5])

def transpose():
    mat = np.mat('1 2; 3 4')

    # using T
    t = mat.T
    assert np.all(t == np.mat('1 3; 2 4'))

    # using .transpose()
    t = mat.transpose()
    assert np.all(t == np.mat('1 3; 2 4'))

def astype():
    # Casting
    # float -> int
    a = np.array([1.1, 2.9])
    a = a.astype(int)
    assert np.array_equal(a, [1, 2])
    assert a.dtype == np.dtype('int32')

    # int -> float
    a = np.array([1, 2])
    a = a.astype(float)
    assert np.array_equal(a, [1., 2.])
    assert a.dtype == np.dtype('float')

def arange():
    # numpy.arange([start, ]stop, [step])
    # similar to MATLAB's stride (start : stride : stop)
    arr = np.arange(2, 10, 3)
    assert np.array_equal(arr, [2, 5, 8])

    # numpy.arange supports float unlike range:
    arr = np.arange(2.1, 10.3, 2.25)
    close = np.isclose(arr, [2.1, 4.35, 6.6, 8.85])
    assert close.all()
    close = np.isclose(arr, [2.2, 4.35, 6.6, 8.85])
    assert not close.all()

def flat():
    # get row-major index
    m = np.matrix('7 8; 9 10')
    assert m.flat[0] == 7
    assert m.flat[1] == 8
    assert m.flat[2] == 9
    assert m.flat[3] == 10

# Convert numpy array to python list
def numpyArrayToPythonList():
    a = np.array([ [1, 2], [3, 4] ])
    l = a.tolist()
    assert l == [[1, 2], [3, 4]]
    assert isinstance(l, list)

# Convert python list to numpy array
def pythonListToNumpyArray():
    array = [1, 2]
    a = np.array(array)
    assert isinstance(a, np.ndarray)
    assert np.array_equal(a, [1, 2])

def mean():
    # [1 2
    #  3 4]
    m = np.mat('1 2; 3 4')
    assert m.mean() == 2.5

    # by row (axis = 0)
    # (1 + 3) / 2 = 2
    row = m.mean(axis=0)
    assert row.flat[0] == 2.0
    assert row.flat[1] == 3.0

    # (1 + 2) / 2 = 1.5
    # by column (axis = 1)
    col = m.mean(axis=1)
    assert col.flat[0] == 1.5
    assert col.flat[1] == 3.5

def base():
    a = np.array([1.1, 2.2])
    c = a.copy()
    v = a.view() # non-owning view of data

    # base() is None if variable owns its data
    assert a.base is None
    assert c.base is None
    assert v.base is not None

def ones():
    # float (default data type)
    a = np.ones(4)
    assert np.array_equal(a, [1.0, 1.0, 1.0, 1.0])

    # int data type
    a = np.ones((2, 2), dtype=np.int32)
    assert np.array_equal(a, [[1, 1], [1, 1]])

    # ones like another matrix
    a = np.zeros([2, 2], dtype=int)
    m = np.ones_like(a)
    assert np.array_equal(m, [[1, 1], [1, 1]])

def add():
    # add/sum two matrices
    m = np.mat('1 2; 3 4')
    n = np.mat('4 5; 6 7')
    s = m + n
    # alt syntax:
    #s = np.add(m, n)

    assert np.array_equal(s, [[5, 7], [9, 11]])

def end():
    # for MATLAB's 'end' index, use -1:
    m = np.array([1, 2, 3])
    assert m[-1] == 3

def reshape():
    # 2x3:
    # [1, 2, 3
    #  4, 5, 6]
    m = np.matrix([[1, 2, 3], [4, 5, 6]])

    # reshape to 3x2
    m2 = m.reshape(3, 2)
    assert np.array_equal(m.flatten(), m2.flatten())

def power():
    m = np.array([1, 2, 3])

    # prefer '**' operator
    m3 = m ** 3
    assert np.array_equal(m3, [1, 8, 27])

    # can also use power() function
    m3 = np.power(m, 3)
    assert np.array_equal(m3, [1, 8, 27])

def countNonzero():
    m = np.matrix([[1, 2, 3], [4, 5, 6]])

    # get even mask
    even = m % 2 == 0
    assert even.dtype == np.dtype('bool')

    # count number of non-zero elements (equivalent to MATLAB's nnz)
    nnz = np.count_nonzero(even)
    assert nnz == 3

def tile():
    # tile can be used to repmat
    # tile(a, (m, n)) is equivalent to:
    # repmat(a, m, n) in MATLAB
    # [0, 1, 2]
    values = np.array([0, 1, 2])

    # tile values into 2 x 3 to create:
    # [0, 1, 2, 0, 1, 2, 0, 1, 2
    #  0, 1, 2, 0, 1, 2, 0, 1, 2]
    newValues = np.tile(values, (2, 3))
    assert np.array_equal(newValues, \
        [ [0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2] ]);

def mode():
    # get most common value in array using unique counts

    # one mode:
    values = np.array([2, 1, 3, 1, 3, 3, 4])
    vals, counts = np.unique(values, return_counts = True)
    counts = np.argwhere(counts == np.max(counts))
    modeValue = vals[counts].flatten().tolist()
    assert len(modeValue) == 1
    assert modeValue[0] == 3

    # two modes:
    values = np.array([2, 2, 1, 1, 3])
    vals, counts = np.unique(values, return_counts = True)
    counts = np.argwhere(counts == np.max(counts))
    modeValue = vals[counts].flatten().tolist()
    assert len(modeValue) == 2
    assert modeValue == [1, 2]

def empty():
    # np.empty is like np.zeros but does not initialize values
    # analagous to malloc vs calloc
    # np.empty is NOT like MATLAB's empty

    arr = np.empty([1, 5000])
    assert arr.sum() != 0

def shuffle():
    # create a 0..N sequence
    highElem = 50
    sequence = np.arange(0, highElem)
    assert np.array_equal(sequence, np.arange(0, highElem))

    # shuffle the sequence
    np.random.shuffle(sequence)
    # verify the order has changed
    assert not np.array_equal(sequence, np.arange(0, highElem))

def delete():
    # delete (remove) elements from numpy array

    # create [5, 6, 7, 8, 9]
    arr = np.arange(5) + 5

    # delete idx=1 from array (value = 6)
    arr = np.delete(arr, 1)
    assert np.array_equal(arr, [5, 7, 8, 9])

    # delete idx=0 and idx=2 from [5, 7, 8, 9] (values = 5, 8)
    arr = np.delete(arr, [0, 2])
    assert np.array_equal(arr, [7, 9])

def deleteMatrix():
    # create 3x3 matrix:
    # [0 1 2
    #  3 4 5
    #  6 7 8]
    matrix = np.arange(9).reshape(3, 3)

    # delete 1st row (axis=0)
    matrix = np.delete(matrix, 1, axis=0)
    assert np.array_equal(matrix, [ [0, 1, 2], [6, 7, 8] ])

    # delete 0th column (axis=1)
    matrix = np.delete(matrix, 0, axis=1)
    assert np.array_equal(matrix, [ [1, 2], [7, 8] ])

def ndim():
    # scalar specifying the number of dimensions of a value

    # 1D
    v = np.arange(5)
    assert v.ndim == 1

    # 1D (empty)
    nul = np.empty(shape=(0,))
    assert nul.ndim == 1

    # 2D
    mat = np.arange(4).reshape(2, 2)
    assert mat.ndim == 2

    # 3D
    threeD = np.arange(12).reshape(2,2,3)
    assert threeD.ndim == 3
    assert threeD.shape == (2, 2, 3)

def maxAndMin():
    # Vector: [0, 1, 2]
    v = np.arange(3)
    assert v.min() == 0
    assert v.max() == 2

    # Matrix: [0, 1
    #          2, 3]
    m = np.arange(4).reshape(2, 2)
    assert m.min() == 0
    assert m.max() == 3

    # Axis = 0: get min/max of each row
    assert m.min(axis = 0).tolist() == [0, 1]

    # Axis = 1: get min/max of each column
    assert m.min(axis = 1).tolist() == [0, 2]
    assert m.max(axis = 1).tolist() == [1, 3]

def full():
    # return array with given shape and type (default data type is np.array(fill_value).dtype)

    # create [10, 10, 10
    #         10, 10, 10]
    m = np.full(shape=[2, 3], fill_value=10, dtype=int)
    assert m.shape == (2, 3)
    assert m.dtype == np.dtype('int32')
    assert np.all(m == 10)

# Returns size of individual element
def itemsize():
    # bool (1 byte)
    v = np.array(True)
    assert v.itemsize == 1
    assert v.dtype == np.dtype('bool')

    # int (4 bytes)
    v = np.arange(1)
    assert v.itemsize == 4
    assert v.dtype == np.dtype('int32')

    # double (8 bytes)
    v = np.arange(1.0)
    assert v.itemsize == 8
    assert v.dtype == np.dtype('float64')

def main():
    arrayCreation()
    matrixCreation()
    matrixIndexing()
    numel()
    shape()
    all()
    flatten()
    iterate()
    matrixMultiplication()
    arithmetic()
    dataType()
    logicalIndexing()
    transpose()
    astype()
    arange()
    flat()
    numpyArrayToPythonList()
    pythonListToNumpyArray()
    mean()
    base()
    ones()
    add()
    end()
    reshape()
    power()
    countNonzero()
    tile()
    mode()
    empty()
    shuffle()
    delete()
    deleteMatrix()
    ndim()
    maxAndMin()
    full()
    itemsize()

if __name__ == '__main__':
    main()
    print('Tests passed!')
