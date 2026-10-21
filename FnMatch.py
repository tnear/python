'''
fnmatch - Unix filename pattern matching
https://docs.python.org/3/library/fnmatch.html

See also: glob.py
'''

import fnmatch

def usage():
    names = ['report.txt', 'notes.txt', 'photo.jpg']
    matched = []
    for name in names:
        # check if name has a txt extension
        match = fnmatch.fnmatch(name, '*.txt')
        if match:
            matched.append(name)

    # the txt files
    assert matched == ['report.txt', 'notes.txt']

def main():
    usage()

if __name__ == '__main__':
    main()
    print(f'\nTests passed for {__file__}!')
