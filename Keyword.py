# keyword — Testing for Python keywords
# https://docs.python.org/3/library/keyword.html

import keyword

def iskeyword():
    assert keyword.iskeyword('def')
    assert keyword.iskeyword('if')
    assert not keyword.iskeyword('__name__')
    assert not keyword.iskeyword('fake')

def kwlist():
    # kwlist is a list of all Python keywords
    assert isinstance(keyword.kwlist, list)
    assert 'False' in keyword.kwlist
    assert 'yield' in keyword.kwlist

# Python 3.9
def issoftkeyword():
    # soft keywords are keywords only under specific contexts
    assert keyword.issoftkeyword('_')
    assert keyword.issoftkeyword('case')
    assert keyword.issoftkeyword('match')

# Python 3.9
def softkwlist():
    assert '_' in keyword.softkwlist
    assert 'case' in keyword.softkwlist
    assert 'match' in keyword.softkwlist

def main():
    iskeyword()
    kwlist()
    issoftkeyword()
    softkwlist()

if __name__ == '__main__':
    main()
    print('Tests passed!')
