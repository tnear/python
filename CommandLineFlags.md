# Command Line Flags

Common command line flags for Python.

## `-c <command`
Use `-c` to run a single python command or statement.
```bash
python -c 'print(1.23)'
```

## `-i` for interactive
Use `-i` to enter into interactive mode after running a python script. This is useful for inspecting variables after a script finishes.
```bash
python -i String.py
```

## `-h` for help
```bash
python -h
```

## `-m <module>`
Use `-m` to run a module as a script. Most common for `pip` and `unittest`.

```bash
# installing
python -m pip install requests

# testing
python -m unittest discover test
```

## `--version`
```bash
$ python --version
Python 3.12.4
```
