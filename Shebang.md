
The shebang (or hashbang) is a special sequence of two characters, `#!`, that must be placed on the first line of a Python script to tell the OS which interpreter to use for execution.

## Best practices
- Place on first line only
- Make the python script executable (`chmod +x script_name.py`)
- Does not support Windows
- Only supports Python scripts (not modules)
- Combine with `if __name__ == "__main__":` so that the code only runs when executed as a script, but not when imported as a module.

## Example
```python
#!/usr/bin/env -S python3 -u
```

- `/usr/bin/env python3`: the standard way to locate where python is installed by using the user's `PATH` environment variable.
- `-S`: split shebang strings. Without this, `env` would look for a program named "python3 -u" (one string)
- `-u`: unbuffered mode: forces `stdout` and `stderr` to be unbuffered (see also `PYTHONUNBUFFERED`)

## Resources
- https://docs.python.org/3/using/cmdline.html
