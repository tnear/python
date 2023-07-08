# io — Core tools for working with streams
# https://docs.python.org/3/library/io.html

import io

def stringIO():
    text = 'Hello, world.\nHow are you?'
    # use the StringIO constructor
    stringStream = io.StringIO(text)

    # use getvalue() to get textual data
    value = stringStream.getvalue()
    assert value == text

    # close buffer when done
    stringStream.close()

def main():
    stringIO()

if __name__ == '__main__':
    main()
    print('Tests passed!')
