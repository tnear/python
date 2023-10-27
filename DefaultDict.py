# Like dictionary but uses a default value for keys which do not exist
# https://docs.python.org/3/library/collections.html

import collections

def basic():
    dd = collections.defaultdict(lambda: 'Not present')
    dd['a'] = 1
    assert dd['a'] == 1
    assert dd['fake_key'] == 'Not present'

    assert list(dd.keys()) == ['a', 'fake_key']

def defaultInteger():
    # defaultdict is useful for incrementing the count of things in map
    words = ["apple", "banana", "orange", "apple", "apple", "banana"]

    wordCount = collections.defaultdict(int) # type int will default to zero
    for word in words:
        wordCount[word] += 1

    assert wordCount['apple'] == 3

    '''
    Note: a regular dictionary must first check if the value is already present:
    wordCount = {}
    for word in words:
        if word not in wordCount:
            wordCount[word] = 0
        wordCount[word] += 1
    '''

def main():
    basic()
    defaultInteger()

if __name__ == '__main__':
    main()
    print('Tests passed!')
