# tempfile — Generate temporary files and directories
# https://docs.python.org/3/library/tempfile.html

import tempfile
import shutil

def get_temp_dir():
    # same as tempfile.tempdir but with function all
    td = tempfile.gettempdir()
    print(f'{td=}')

def temp_dir():
    # same as tempfile.gettempdir() but using member variable
    td = tempfile.tempdir
    print(f'{td=}')

def make_temp_dir():
    # create a temporary directory with a prefix,
    # ex: /tmp/my_test_7t41dye7
    td = tempfile.mkdtemp(prefix='my_test_')
    print(f'{td=}')
    shutil.rmtree(td)

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
