'''
pwd - The password database
https://docs.python.org/3/library/pwd.html

UNIX-only utility for /etc/passwd
'''

import pwd

# pwd.getpwall returns all password database entries
# in arbitrary order
def getpwall():
    all_entries = pwd.getpwall()
    all_user_names = [x.pw_name for x in all_entries]
    assert 'tnear' in all_user_names

def main():
    getpwall()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
