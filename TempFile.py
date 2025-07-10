# tempfile — Generate temporary files and directories
# https://docs.python.org/3/library/tempfile.html

import tempfile
import shutil

def get_temp_dir():
    # same as tempfile.tempdir but with function call
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

# NamedTemporaryFile creates a uniquely named temporary file with parameters
# for prefix and suffix. The file is deleted when it scope ends (fixture).
def named_temporary_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.dat', prefix='my_file_') as f:
        # get file name, ex: '/tmp/my_file_<rand>.dat'
        print(f.name)

        # write to file
        f.write('hello')
        f.flush()

        # file is deleted here

def main():
    get_temp_dir()
    temp_dir()
    make_temp_dir()
    temp_dir_context_manager()
    named_temporary_file()

if __name__ == '__main__':
    main()
    print('Tests passed!')
