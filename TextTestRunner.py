import unittest
import sys
import time
from unittest.runner import TextTestResult, TextTestRunner

class VerboseTestResult(TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.start_time = 0

    def startTest(self, test):
        super().startTest(test)
        test_name = self.getDescription(test)
        print(f'\n[SETUP] {test_name}', file=sys.stderr)
        self.start_time = time.time()

    def stopTest(self, test):
        test_name = self.getDescription(test)
        elapsed = time.time() - self.start_time
        print(f'\n[TEARDOWN] {test_name} (duration {elapsed:.3f}s)', file=sys.stderr)
        super().stopTest(test)

    def getDescription(self, test):
        # Get the test class name and method name
        class_name = test.__class__.__name__
        method_name = test._testMethodName
        return f'{class_name}.{method_name}'

class CustomTestRunner(TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resultclass = VerboseTestResult

# Create a utility module to make it easy to use in all test files
def run_tests(test_case_class):
    '''
    A utility function that can be imported and used to run tests
    with our custom runner.

    Usage:
        if __name__ == '__main__':
            from test_utils import run_tests
            run_tests(MyTestCase)
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    runner = CustomTestRunner(verbosity=1)
    result = runner.run(suite)
    return result

# Example of a test case using the custom runner
class SampleTest(unittest.TestCase):
    def test_example(self):
        time.sleep(0.01)
        self.assertEqual(1, 1)

    def test_example2(self):
        test_cases = [
            (1, 1),
            (-1, -1)
        ]
        for expected, actual in test_cases:
            with self.subTest(expected=expected, actual=actual):
                self.assertEqual(expected, actual)

    def test_another_example(self):
        time.sleep(0.005)
        self.assertTrue(True)


# Example usage
if __name__ == '__main__':
    run_tests(SampleTest)
