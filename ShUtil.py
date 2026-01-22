'''
shutil - High-level file operations (shell utilities)
https://docs.python.org/3/library/shutil.html
'''

import shutil

def which():
    # find location of 'cd' command
    result = shutil.which('cd')
    assert result == '/usr/bin/cd'

    # invalid command returns None
    result = shutil.which('fake_cmd')
    assert result is None

def disk_usage():
    usage = shutil.disk_usage('/')
    assert usage.total > 0
    assert usage.used > 0
    assert usage.free > 0

def main():
    which()
    disk_usage()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
