# unittest — Unit testing framework
# https://docs.python.org/3/library/unittest.html

import unittest

class Exceptions(unittest.TestCase):
    @staticmethod
    def raiseException(arg1):
        raise Exception(f'Caught exception: {arg1}!')

    def testException(self):
        self.assertRaises(Exception, Exceptions.raiseException, 'argument')

    def testExceptionMessage(self):
        # use a context manager to raise the exception
        with self.assertRaises(Exception) as contextMgr:
            Exceptions.raiseException('argument')

        # use the context manager to get the message
        msg = contextMgr.exception.args[0]
        assert msg == 'Caught exception: argument!'

class Fixtures(unittest.TestCase):
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

# uncommenting next line will skip the entire class
#@unittest.skip('Skipping entire class')
class Skip(unittest.TestCase):
    @unittest.skip('Unconditional skip')
    def testNothing(self):
        self.fail('Unreachable')

    @unittest.skipIf(2 > 1, 'Conditional skip')
    def testNothing2(self):
        self.fail('Unreachable')

    # Note: methods must begin with 'test'
    # This test does not and therefore is not called by the runner
    # Prefer unittest.skip over this
    def fakeTest(self):
        self.fail('Unreachable')

paramList = [1, 2, 3]
class Parameterization(unittest.TestCase):
    def testParameters(self):
        for value in paramList:
            # use subTest to parameterize a test point
            with self.subTest():
                self.assertGreater(value, 0)

def creation():
    # create TestCase instance for interactive use
    testCase = unittest.TestCase()
    testCase.assertTrue(False)

if __name__ == '__main__':
    unittest.main()

    # Note: this line will allow for profiling with cProfile:
    # unittest.main(module='UnitTest') # 'UnitTest' is module name
