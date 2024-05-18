import unittest

class TestDemo1(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 2

    def test_arithmetic(self):
        print("test_arithmetic")
        print(f"a = {self.a}")
        print(f"b = {self.b}")
        self.a = self.a + self.a
        self.assertEqual(self.a, self.b)

    def test_compare(self):
        print("test_compare")
        print(f"a = {self.a}")
        print(f"b = {self.b}")
        self.a = self.b - self.a
        self.assertTrue(self.a < 2, f"{self.a} is not lesser than 2")
    @unittest.expectedFailure
    def test_failure_absent_parameter(self):
        self.a = self.c + self.b

    @unittest.expectedFailure
    def test_failure_division_by_zero(self):
        self.a = self.b / 0
        
class TestDemo(unittest.TestCase):

    def test_arithmetic(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skip("It is not needed at this test cycle")
    def test_compare(self):
        a = 5
        self.assertTrue(a < 2, f"{a} is not lesser than 2")
        
    assert 1 < 5, "False condition"

if __name__ == '__main__':
    unittest.main()
