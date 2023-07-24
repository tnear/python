import numpy as np

def placeholder():
    # can use '...' (in addition to pass) for unimplemented code
    ...

def dataType():
    assert ... is Ellipsis

def typeHint():
    # tuple of variable size
    t: tuple[int, ...] = (1, 2, 3)
    assert isinstance(t, tuple)

def sliceArray():
    # create matrix [1, 2
    #                3, 4
    #                5, 6]
    arr = np.array([ [1, 2], [3, 4], [5, 6] ])

    # get first column using '...'
    assert arr[..., 1].tolist() == [2, 4, 6]

    # alt syntax using ':' (MATLAB)
    assert arr[:, 1].tolist() == [2, 4, 6]

def main():
    placeholder()
    dataType()
    typeHint()
    sliceArray()

if __name__ == '__main__':
    main()
    print('Tests passed!')
