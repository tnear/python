# textwrap — Text wrapping and filling
# https://docs.python.org/3/library/textwrap.html

import textwrap

def fillExample():
    s = 'long line 123 long line 456 long line 789 long line 101'
    # wrap lines at 20 characters
    result = textwrap.fill(s, width=20)
    print(result)
    assert result == 'long line 123 long\nline 456 long line\n789 long line 101'

def dedentExample():
    # dedent removes common leading whitespace in every line of text
    # note how lines 1 and 2 have the same leading whitespace.
    # without dedent, the multiline string would have many spaces before each line.
    s = textwrap.dedent('''
                        Line 1
                        Line 2
                        ''').strip()
    assert s == 'Line 1\nLine 2'

def main():
    fillExample()
    dedentExample()

if __name__ == '__main__':
    main()
    print('Tests passed!')
