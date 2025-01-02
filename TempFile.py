# tempfile — Generate temporary files and directories
# https://docs.python.org/3/library/tempfile.html

import shutil
import tempfile

def get_temp_dir():
    # same as tempfile.tempdir but with function all
    dir = tempfile.gettempdir()
    print(f'{dir=}')

def temp_dir():
    # same as tempfile.gettempdir() but using member variable
    td = tempfile.tempdir
    print(f'{td=}')

def make_temp_dir():
    # create a temporary directory with a prefix,
    # ex: /tmp/my_test_7t41dye7
    temp_dir = tempfile.mkdtemp(prefix='my_test_')
    print(f'{temp_dir=}')
    shutil.rmtree(temp_dir)

def temp_dir_context_manager():
    # create temporary directory which is automatically
    # removed when scope ends
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f'{temp_dir=}')

def main():
    get_temp_dir()
    temp_dir()
    make_temp_dir()
    temp_dir_context_manager()

if __name__ == '__main__':
    main()
    print('Tests passed!')
