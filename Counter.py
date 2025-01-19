# Counter: maintains count of elements inside
# Similar to map where the value is the count.
# Duplicates are permitted
# https://docs.python.org/3/library/collections.html

from collections import Counter

def listConstructor():
    c = Counter(['a', 'b', 'a', 'b', 'b'])
    assert c['a'] == 2
    assert c['b'] == 3
    assert list(c.keys()) == ['a', 'b']
    assert list(c.values()) == [2, 3]

def dictionaryConstructor():
    c = Counter({'a': 17, 2: 25})
    assert list(c.keys()) == ['a', 2]
    assert list(c.values()) == [17, 25]

def keywordConstructor():
    c = Counter(a=101, b=102)
    assert list(c.keys()) == ['a', 'b']
    assert list(c.values()) == [101, 102]

def update():
    # update adds elements
    # initialize a's count to 101 and b's count to 102
    c = Counter(a=101, b=102)
    assert list(c.keys()) == ['a', 'b']

    # initialize new element 'c' with count 103
    c.update(c=103)
    assert list(c.values()) == [101, 102, 103]
    assert list(c.keys()) == ['a', 'b', 'c']

    # add 2 to c count
    c.update(c=2)
    assert list(c.values()) == [101, 102, 105]

    # initialize d to count = 0
    c.update(d=0)
    assert list(c.values()) == [101, 102, 105, 0]
    assert list(c.keys()) == ['a', 'b', 'c', 'd']

    # initialize e to negative count
    c.update(e=-2)
    assert list(c.values()) == [101, 102, 105, 0, -2]
    assert list(c.keys()) == ['a', 'b', 'c', 'd', 'e']

def find_duplicates():
    # create a list with duplicate elements
    items = [3, 1, 2, 4, 2, 1, 0]

    # use Counter to track each element's count.
    # (note: do not use list.count because it is a linear scan)
    duplicates = [item for item, count in Counter(items).items() if count > 1]
    assert duplicates == [1, 2]

def main():
    listConstructor()
    dictionaryConstructor()
    keywordConstructor()
    update()
    find_duplicates()

if __name__ == '__main__':
    main()
    print('Tests passed!')
