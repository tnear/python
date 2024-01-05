# subprocess — Subprocess management.
# subprocess allows you to spawn new processes.
# https://docs.python.org/3/library/subprocess.html

import subprocess

def basic():
    # run 'ipconfig' and get its output and return code (0 = success)
    completedProcess = subprocess.run(['ipconfig'], text=True, capture_output=True)
    assert completedProcess.returncode == 0
    assert 'Ethernet' in completedProcess.stdout

def multipleArguments():
    # use a list of strings to pass in additional arguments
    completedProcess = subprocess.run(['ipconfig', '/all'], text=True, capture_output=True)
    assert completedProcess.returncode == 0
    assert 'Host Name' in completedProcess.stdout

def main():
    basic()
    multipleArguments()

if __name__ == '__main__':
    main()
    print('Tests passed!')
