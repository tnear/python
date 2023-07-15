# unittest — Unit testing framework
# https://docs.python.org/3/library/unittest.html

import unittest

class TestExceptions(unittest.TestCase):
    @staticmethod
    def raiseException(arg1):
        raise Exception(f'Caught exception: {arg1}!')

    # Note: methods must begin with 'test'
    # This test does not and therefore is not called by the runner
    # Todo: move to 'skip' section
    def fakeTest(self):
        self.assertTrue(False)

    def testException(self):
        self.assertRaises(Exception, TestExceptions.raiseException, 'argument')

    def testExceptionMessage(self):
        # use a context manager to raise the exception
        with self.assertRaises(Exception) as contextMgr:
            TestExceptions.raiseException('argument')

        # use the context manager to get the message
        msg = contextMgr.exception.args[0]
        assert msg == 'Caught exception: argument!'

class TestFixtures(unittest.TestCase):
    # 'setUp' method will be called before each test point
    def setUp(self):
        print('setUp method fixture called')

    # 'tearDown' method will be called after each test point
    def tearDown(self):
        print('tearDown method fixture called')

    # 'setUpClass' is called once at the beginning of a class's execution
    @classmethod
    def setUpClass(self):
        print('\nsetUpClass class fixture called')

    # 'tearDownClass' is called once at the end of a class's execution
    @classmethod
    def tearDownClass(self):
        print('tearDownClass class fixture called')

    def testOne(self):
        print('test one')

    def testTwo(self):
        print('test two')

if __name__ == '__main__':
    unittest.main()

    # Note: this line will allow for profiling with cProfile:
    # unittest.main(module='UnitTest') # 'UnitTest' is module name
