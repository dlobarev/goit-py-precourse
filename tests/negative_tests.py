import unittest
from numbers import TestDemoNumbers
from strings import  TestDemoStrings

if __name__ == '__main__':
    negative_tests_suite = unittest.TestSuite()

    negative_tests_suite.addTest(TestDemoStrings('test_failure_concatenation_with_number'))
    negative_tests_suite.addTest(TestDemoNumbers('test_failure_absent_parameter'))
    negative_tests_suite.addTest(TestDemoNumbers('test_failure_division_by_zero'))

    runner = unittest.TextTestRunner()
    runner.run(negative_tests_suite)

