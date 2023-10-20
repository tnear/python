# Coverage

https://coverage.readthedocs.io/

Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

## Installation
```powershell
> python -m pip install coverage
```

## Collect coverage
If tests are normally run with `python -m unittest`, replace to this to collect coverage:

```powershell
> coverage run -m unittest
```

## Coverage report

### Plaintext coverage report
```powershell
> coverage report -m
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
Rule.py                       112      0   100%
testMatchCaseSensitive.py      42      1    98%   54
testMatchExact.py              27      1    96%   39
testMatchNone.py               17      1    94%   31
testMatchPrefix.py             39      1    97%   156
testMatchSuffix.py             49      1    98%   135
testMatchWhitelist.py          32      1    97%   51
testRule.py                   115      2    98%   155, 166
---------------------------------------------------------
TOTAL                         433      8    98%
```

### Detailed coverage report
```powershell
> coverage html
```
