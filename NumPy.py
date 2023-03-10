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

def all():
    arr = np.array([2, 4, 5, 6, 8])
    # method:
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
    # 2D
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
    t = np.mat('1 2; 3 4').T
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

# Convert numpy array to python array
def numpyArrayToPythonArray():
    a = np.array([ [1, 2], [3, 4] ])
    l = a.tolist()
    assert l == [[1, 2], [3, 4]]
    assert isinstance(l, list)

def pythonArrayToNumpyArray():
    a = np.asarray([1, 2])
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

def main():
    arrayCreation()
    matrixCreation()
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
    numpyArrayToPythonArray()
    pythonArrayToNumpyArray()
    mean()
    base()
    ones()

if __name__ == '__main__':
    main()
    print('Tests passed!')
