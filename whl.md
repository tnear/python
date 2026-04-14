# whl

A `.whl` file (wheel) is a standard format for distributing Python packages. It is a pre-built Python package that can be installed using `pip`.

## What is a wheel?
A wheel is like a ZIP archive which contains Python code and metadata.

## Managing
```bash
# install wheel
$ pip install mypackage.whl

# building wheel
$ pip install build
$ python -m build
```

### Filenames
```
mypackage-1.0.0-cp310-cp310-manylinux_x86_64.whl
```

- `mypackage`: package name
- `1.0.0`: version
- `cp310`: Python version (CPython 3.10)
- `manylinux_x86_64`: platform

#### Pure-Python wheel
```
Jinja2-3.0.0a1-py3-none-any.whl
```

- `py3-none-any`: installs on any platform (called pure-Python wheel)

## Resources
- https://realpython.com/python-wheels/#wheels-make-things-go-fast
