# DefaultDict.py
# Like dictionary but uses a default value for keys which do not exist
# https://docs.python.org/3/library/collections.html

import collections

def f():
    dd = collections.defaultdict(lambda: 'Not present')
    dd['a'] = 1
    assert dd['a'] == 1
    assert dd['fake_key'] == 'Not present'

    assert list(dd.keys()) == ['a', 'fake_key']

def main():
    f()

if __name__ == '__main__':
    main()
    print('Tests passed!')
