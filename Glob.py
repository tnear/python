'''
glob — Unix style pathname pattern expansion
https://docs.python.org/3/library/glob.html
'''

import glob

def globPattern():
    # get all python files in current directory
    pyFiles = glob.glob('*.py')
    assert 'Glob.py' in pyFiles

def numberRange():
    # get files of form file1.txt, file2.txt, file3.txt
    fileRange = glob.glob('file[1-3].txt')

    # this repository has none
    assert fileRange == []

def main():
    globPattern()
    numberRange()

if __name__ == '__main__':
    main()
    print('Tests passed!')
