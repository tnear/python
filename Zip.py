# Zip: Iterate over several iterables in parallel, producing tuples with an item from each one.
# https://docs.python.org/3/library/functions.html

def sameLength():
    languages = ['Java', 'Python', 'JavaScript']
    versions = [14, 3, 6]
    result = zip(languages, versions)
    assert list(result) == [('Java', 14), ('Python', 3), ('JavaScript', 6)]

def diffLength():
    # shortest length determines result length
    four = [1, 2, 3, 4]
    three = ['one', 'two', 'three']
    result = zip(four, three)
    assert len(list(result)) == 3

def unzip():
    x = (1, 2)
    y = (3, 4)
    result = zip(x, y)

    # use *zippedResult to undo a zip
    x1, y1 = zip(*result)
    assert x1 == x
    assert y1 == y

    # unzipping is a one-time operation
    result2 = zip(*result)
    assert len(list(result2)) == 0

# useful technique when creating a custom error message
def findFirstUnsortedElement():
    # starting list which is not sorted
    a = ['abc', 'zzz', 'def']

    # sort and make a copy
    aSorted = sorted(a)

    # iterate through both using zip. The first difference will be where
    # the original list was not sorted.
    for original, sortedItem in zip(a, aSorted):
        if original != sortedItem:
            assert original == 'zzz' and sortedItem == 'def'
            break

def main():
    sameLength()
    diffLength()
    unzip()
    findFirstUnsortedElement()

if __name__ == '__main__':
    main()
    print('Tests passed!')
