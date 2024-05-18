import unittest

class TestDemoNumbers(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_arithmetic(self):
        self.a = self.a + self.a
        self.assertEqual(self.a, self.b)

    def test_compare(self):
        self.a = self.b - self.a
        self.assertTrue(self.a < 2, f"{self.a} is not lesser than 2")

    @unittest.expectedFailure
    def test_failure_absent_parameter(self):
        self.a = self.c + self.b

    @unittest.expectedFailure
    def test_failure_division_by_zero(self):
        self.a = self.b / 0

if __name__ == '__main__':
    unittest.main()
