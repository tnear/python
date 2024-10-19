# pathlib — Object-oriented filesystem paths
# https://docs.python.org/3/library/pathlib.html

# Note: prefer pathlib over os.path

import pathlib
import platform

def cwd():
    # Path.cwd() returns a Path object instead of string like os.getcwd()
    pwd = pathlib.Path.cwd()

    assert pwd.name == 'python'

    if platform.system() == 'Windows':
        assert isinstance(pwd, pathlib.WindowsPath)

def exists():
    file = 'Pathlib.py'
    fakeFile = 'FakeFile.py'

    assert not pathlib.Path(fakeFile).exists()
    assert pathlib.Path(file).exists

def mkdir():
    dir = 'my_dir'
    assert not pathlib.Path(dir).is_dir()

    # create a directory
    pathlib.Path(dir).mkdir()
    assert pathlib.Path(dir).is_dir()

    # remove the directory
    pathlib.Path(dir).rmdir()
    assert not pathlib.Path(dir).is_dir()

def parent():
    # Gets directory name
    # equivalent to os.path.dirname()
    pwd = pathlib.Path.cwd()
    parent = pathlib.Path(pwd).parent
    assert len(parent.name)

def unlink():
    # unlink can be used to remove files
    file = 'a.txt'
    assert not pathlib.Path(file).exists()
    with open(file, 'w', encoding='utf-8') as f:
        f.write('hello')

    assert pathlib.Path(file).exists()
    # remove (unlink) file
    pathlib.Path(file).unlink()
    assert not pathlib.Path(file).exists()

def rename():
    file = 'a.txt'
    fileNew = 'b.txt'
    assert not pathlib.Path(file).exists()
    assert not pathlib.Path(fileNew).exists()
    with open(file, 'w', encoding='utf-8') as f:
        f.write('hello')

    # Rename file
    pathlib.Path(file).rename(fileNew)

    # Verify rename was successful
    assert not pathlib.Path(file).exists()
    assert pathlib.Path(fileNew).exists()

    # remove file
    pathlib.Path(fileNew).unlink()

def main():
    cwd()
    exists()
    mkdir()
    parent()
    unlink()
    rename()

if __name__ == '__main__':
    main()
    print('Tests passed!')
