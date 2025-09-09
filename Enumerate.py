# enumerate() returns both index and element when iterating

def enumerateOneArg():
    li = ['a', 'b', 'c']

    # Return (idx, elem) in one tuple
    data = []
    for tup in enumerate(li):
        data.append(tup)

    assert data == [(0, 'a'), (1, 'b'), (2, 'c')]

def enumerateTwoArgs():
    li = ['a', 'b', 'c', 'd']

    # Return idx, elem in 2 args
    idxs = []
    elems = []
    for idx, elem in enumerate(li):
        idxs.append(idx)
        elems.append(elem)

    assert idxs == [0, 1, 2, 3]
    assert elems == ['a', 'b', 'c', 'd']

def start():
    elems = ['a', 'b', 'c']
    # use 'start' to specify a start index
    for idx, elem in enumerate(elems, start=3):
        assert idx >= 3
        assert elem in elems

def main():
    enumerateOneArg()
    enumerateTwoArgs()
    start()

if __name__ == '__main__':
    main()
    print('Tests passed!')
