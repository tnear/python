import os

def pwd():
    pwd = os.getcwd()
    assert 'python' in pwd

def path():
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

def main():
    pwd()
    path()
    listdir()
    name()
    getsize()
    getpid()

if __name__ == '__main__':
    main()
    print('Tests passed!')
