# enumerate() returns both element and its index
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

def main():
    enumerateOneArg()
    enumerateTwoArgs()

if __name__ == '__main__':
    main()
    print('Tests passed!')
