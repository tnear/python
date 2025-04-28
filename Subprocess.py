# subprocess — Subprocess management.
# subprocess allows you to spawn new processes.
# https://docs.python.org/3/library/subprocess.html

import subprocess

def basic():
    # run a command and get its output and return code (0 = success)
    completedProcess = subprocess.run(['ls'], text=True, capture_output=True)
    assert completedProcess.returncode == 0
    assert 'Subprocess.py' in completedProcess.stdout

def multipleArguments():
    # use a list of strings to pass in additional arguments
    completedProcess = subprocess.run(['ls', '-l'], text=True, capture_output=True)
    assert completedProcess.returncode == 0
    assert 'tnear' in completedProcess.stdout

def error_command():
    completed_process = subprocess.run(['ls', '-fake_flag'], text=True, capture_output=True)
    assert completed_process.returncode != 0
    assert 'invalid option' in completed_process.stderr

def check_output():
    # check_output is equivalent to subprocess.run(..., check=True, stdout=PIPE).
    # check_output raises an exception (instead of setting returncode) for errors.
    # check_output returns bytes
    byte_array = subprocess.check_output(['ls'])
    assert isinstance(byte_array, bytes)
    string = byte_array.decode()
    assert 'Subprocess.py' in string

def main():
    basic()
    multipleArguments()
    error_command()
    check_output()

if __name__ == '__main__':
    main()
    print('Tests passed!')
