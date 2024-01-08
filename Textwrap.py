# textwrap — Text wrapping and filling
# https://docs.python.org/3/library/textwrap.html

import textwrap

def fill():
    s = 'long line 123 long line 456 long line 789 long line 101'
    # wrap lines at 20 characters
    result = textwrap.fill(s, width=20)
    print(result)
    assert result == 'long line 123 long\nline 456 long line\n789 long line 101'

def main():
    fill()

if __name__ == '__main__':
    main()
    print('Tests passed!')
