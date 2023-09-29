# venv — Creation of virtual environments
# https://docs.python.org/3/library/venv.html

import sys

def creation():
    # create a virtual environment directory in pwd called 'myEnv':
    # python -m venv myEnv

    # activate (Windows):
    # > .\myEnv\Scripts\activate

    # activate (Linux):
    # $ source myEnv/bin/activate

    # install dependencies:
    # (myEnv) $ pip install -r requirements.txt

    # verify installation:
    # (myEnv) $ pip list

    # deactivate when done:
    # (myEnv) $ deactivate

    print(sys.prefix)
    print(sys.base_prefix)

def main():
    creation()

if __name__ == '__main__':
    main()
    print('Tests passed!')
