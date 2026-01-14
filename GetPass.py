'''
getpass - Portable password input
https://docs.python.org/3/library/getpass.html
'''

import getpass
import os
import pwd

def get_user():
    # getuser returns current user name
    username = getpass.getuser()

    # longer syntax using os and pwd
    uid = os.getuid()
    assert username == pwd.getpwuid(uid).pw_name

def main():
    get_user()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
