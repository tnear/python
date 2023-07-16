# unittest.mock — mock object library
# https://docs.python.org/3/library/unittest.mock.html
# https://realpython.com/python-mock-library/

import unittest.mock
import datetime

# create some dates for testing
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

def creation():
    mock = unittest.mock.Mock()
    assert isinstance(mock, unittest.mock.Mock)

    # Attributes and methods are created as you access them:
    mock.newAttribute = 1
    assert mock.newAttribute == 1

    mock.newMethod = lambda a : a + 1
    assert mock.newMethod(1) == 2

    # Mock method return values are also mock
    newMock = mock.lazyFunction()
    assert isinstance(newMock, unittest.mock.Mock)

    newMock = mock.fcn().any('any', 'args', 'are', 'supported').fcn(0).works()
    assert isinstance(newMock, unittest.mock.Mock)

def methods():
    # create mock json object
    json = unittest.mock.Mock()

    # assert loads() has not yet been called
    json.loads.assert_not_called()

    # Synthesize and call a 'loads' function
    json.loads('{"key": "value"}')

    # assert loads() was called (once and with certain arguments)
    json.loads.assert_called()
    json.loads.assert_called_once()
    json.loads.assert_called_with('{"key": "value"}')

    # call loads() a second time
    json.loads('{"key2": "value2"}')
    assert json.loads.call_count == 2

def returnValue():
    # set 'datetime' to be a mock object instead of a module
    datetime = unittest.mock.Mock()

    def isWeekday():
        today = datetime.datetime.today()
        return 0 <= today.weekday() < 5

    # set today() return value to be a weekday
    datetime.datetime.today.return_value = tuesday

    # every day is now Tuesday, so this test always passes
    assert isWeekday()

    # change day to Saturday
    datetime.datetime.today.return_value = saturday
    assert not isWeekday()

def sideEffect():
    # Create mock with KeyError side effect
    mock = unittest.mock.Mock(side_effect=KeyError('foo'))

    # verify KeyError when calling mock()
    testCase = unittest.TestCase()
    testCase.assertRaises(KeyError, lambda: mock())
    testCase.assertRaises(KeyError, lambda: mock([1, 2, 3]))

def sideEffectFunction():
    mock = unittest.mock.Mock()

    # side-effect function which increments argument
    def customSideEffect(arg):
        return arg + 1

    # set side_effect
    mock.side_effect = customSideEffect

    # verify the side effect increment behavior
    assert mock(1) == 2
    assert mock(2) == 3

def main():
    creation()
    methods()
    returnValue()
    sideEffect()
    sideEffectFunction()

if __name__ == '__main__':
    main()
    print('Tests passed!')
