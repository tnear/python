# A container which can be accessed both by:
# 1. index (like tuple) and
# 2. key (like dictionary)

import collections

def basic():
    student = collections.namedtuple('Student', ['name', 'age', 'gender'])
    s = student('Alice', 99, False)

    # access index
    assert s[0] == 'Alice'
    assert s[1] == 99
    assert s[2] == False

    # access name
    assert s.name == 'Alice'
    assert s.age == 99
    assert s.gender == False

    # use getattr
    assert getattr(s, 'name') == 'Alice'
    assert getattr(s, 'age') == 99
    assert getattr(s, 'gender') == False

def main():
    basic()

if __name__ == '__main__':
    main()
    print('Tests passed!')
