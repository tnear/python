# os — Miscellaneous operating system interfaces
# https://docs.python.org/3/library/os.html
import os

def pwd():
    pwd = os.getcwd()
    assert 'python' in pwd

def dirname():
    p = os.path.dirname(os.getcwd())
    assert p.endswith('Programming')

def listdir():
    files = os.listdir()
    assert 'OS.py' in files

def name():
    assert 'nt' in os.name

def getsize():
    size = os.path.getsize('OS.py')
    assert size > 500

def getpid():
    pid = os.getpid()
    assert pid > 0

def cpu_count():
    # Returns number of cores on machine
    cpuCount = os.cpu_count()
    assert cpuCount >= 2

def system():
    # Execute OS system calls
    os.system('whoami')

def exists():
    file = 'a.txt'
    assert not os.path.exists(file)
    with open(file, 'w') as f:
        f.write('hello')

    assert os.path.exists(file)
    os.remove(file)
    assert not os.path.exists(file)

def remove():
    file = 'a.txt'
    assert not os.path.exists(file)
    with open(file, 'w') as f:
        f.write('hello')

    assert os.path.exists(file)
    os.remove(file)
    assert not os.path.exists(file)

def makedirs():
    mydir = 'dir1/dir2/dir3'
    assert not os.path.isdir(mydir)

    # Create nested sub-directories
    os.makedirs(mydir)
    assert os.path.isdir(mydir)

    # Cleanup using removedirs()
    os.removedirs(mydir)
    assert not os.path.isdir(mydir)

def main():
    pwd()
    dirname()
    listdir()
    name()
    getsize()
    getpid()
    cpu_count()
    system()
    exists()
    remove()
    makedirs()

if __name__ == '__main__':
    main()
    print('Tests passed!')
