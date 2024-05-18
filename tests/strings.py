import unittest

class TestDemoStrings(unittest.TestCase):
    def setUp(self):
        self.a = "Hello"
        self.b = "World"

    def test_concatenation(self):
        self.a = self.a + " " + self.b
        self.assertEqual("Hello World", self.a)

    def test_split(self):
        c = "Hello World".split()
        self.assertEqual([self.a, self.b], c)

    @unittest.expectedFailure
    def test_failure_concatenation_with_number(self):
        self.a = self.b + 0

if __name__ == '__main__':
    unittest.main()
