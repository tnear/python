# Counter: maintains count of elements inside
# Similar to multiset or multimap
# Duplicates are permitted

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
    c = Counter(a=101, b=102)
    assert list(c.keys()) == ['a', 'b']
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

def main():
    listConstructor()
    dictionaryConstructor()
    keywordConstructor()
    update()

if __name__ == '__main__':
    main()
    print('Tests passed!')
