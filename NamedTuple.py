# A container which can be accessed both by:
# 1. index (like tuple) and
# 2. key (like dictionary)
# https://docs.python.org/3/library/collections.html

import collections

def basic():
    student = collections.namedtuple('Student', ['name', 'age', 'gender'])
    s = student('Alice', 99, False)

    # access index
    assert s[0] == 'Alice'
    assert s[1] == 99
    assert not s[2]

    # access name
    assert s.name == 'Alice'
    assert s.age == 99
    assert not s.gender

    # use getattr
    assert getattr(s, 'name') == 'Alice'
    assert getattr(s, 'age') == 99
    assert not getattr(s, 'gender')

def main():
    basic()

if __name__ == '__main__':
    main()
    print('Tests passed!')
