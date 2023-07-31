# UserString: wrapper around string object which allows customization of methods
# https://docs.python.org/3/library/collections.html

import collections

class MyString(collections.UserString):
    # Custom append which adds word (append)
    def append(self, s):
        self.data += '(append)' + s + ' '

def basic():
    s = MyString('My string')
    assert '(append)' not in s

    s.append('example')

    assert '(append)' in s

def main():
    basic()

if __name__ == '__main__':
    main()
    print('Tests passed!')
