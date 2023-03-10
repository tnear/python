# UserString.py
# Wrapper around string object which allows customization of methods

import collections

class MyString(collections.UserString):
    # Custom append which adds word (append)
    def append(self, s):
        self.data += '(append)' + s + ' '

def f():
    s = MyString('My string')
    assert '(append)' not in s

    s.append('example')

    assert '(append)' in s

def main():
    f()

if __name__ == '__main__':
    main()
    print('Tests passed!')
