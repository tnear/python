# shlex — Shell lexical analysis
# https://docs.python.org/3/library/shlex.html

import shlex

def split():
    command_string = 'ls -l -a "my directory"'

    # Split the string on whitespace
    arguments = shlex.split(command_string)

    assert arguments == ['ls', '-l', '-a', 'my directory']

def join():
    arguments = ['echo', '-n', 'Multiple words']

    command = shlex.join(arguments)
    assert command == "echo -n 'Multiple words'"

def quote():
    # Return a shell-escaped version of the string s.
    filename = 'somefile; rm -rf ~'

    # use quote() to created a safe quoted string
    quotedFile = shlex.quote(filename)

    # note the inner single (hard) quotes
    assert quotedFile == "'somefile; rm -rf ~'"

def main():
    split()
    join()
    quote()

if __name__ == '__main__':
    main()
    print('Tests passed!')
