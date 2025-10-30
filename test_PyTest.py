'''
pytest is a third-party testing framework.
pytest discovers tests by looking for functions prefixed with 'test_'
'''

import pytest

# to run entire file:
# pytest <file>

'''
Common command line flags:
-v, --verbose    = show each test name
-s, --capture=no = display stdout
-q, --quiet      = decrease verbosity
--collect-only   = lists tests in order they will be run
-m mark_name     = run test by mark name
'''

def add_one(x):
    return x + 1

# raises exception
def divide_with_raise(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

# to run a specific test point:
# pytest test_PyTest.py::test_answer (non-class test)
# pytest test_PyTest.py::TestClass::test_one (class test)
def test_answer():
    assert add_one(3) == 4

# use pytest.raises() context manager to verify exceptions
def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide_with_raise(10, 0)
    # verify string
    assert str(exc_info.value) == 'Cannot divide by zero'

# To group tests into a class, you must prefix your class name with 'Test'.
# (classes which do not begin with 'Test' will be skipped).
# No subclass is required.
class TestClass:
    # https://docs.pytest.org/en/stable/getting-started.html
    def test_one(self):
        x = 'hello'
        assert 'h' in x

class TestParameter:
    # parameterized tests. Use comma separated strings in decorator
    # which match to the test function arguments.
    @pytest.mark.parametrize('number,expected', [
        # the body of parametrize uses tuples which will correspond to
        # function arguments
        (2, 4),
        (3, 9),
        (4, 16),
    ])
    def test_square(self, number, expected):
        assert number * number == expected

    # this method does not have the decorator, so it is a regular test
    def test_non_parameterized_test(self):
        pass

# exhaustive parameter combinations by using multiple 'parametrize' lines
@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['a', 'b'])
@pytest.mark.parametrize('z', [True, False])
def test_combinations(x, y, z):
    # print(f'Testing with: x={x}, y={y}, z={z}')
    pass
