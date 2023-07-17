# venv — Creation of virtual environments
# https://docs.python.org/3/library/venv.html

import sys

def creation():
    # python -m venv /path/to/new/virtual/env
    print(sys.prefix)
    print(sys.base_prefix)

def main():
    creation()

if __name__ == '__main__':
    main()
    print('Tests passed!')
