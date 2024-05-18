import unittest
from password_checker.password_checker import PasswordChecker

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.pc = PasswordChecker()
    
    def test_Alice(self):
        name = 'Alice'
        passwd = 'C00peR'
        usr = self.pc.check_password(passwd)
        self.assertEqual(name, usr)

    def test_Carl(self):
        name = 'Carl'
        passwd = 'ClariNet'
        usr = self.pc.check_password(passwd)
        self.assertEqual(name, usr)

    def test_Add_John(self):
        name = 'John'
        passwd = 'SGRed4!'
        self.pc.add_user(name, passwd)
        usr = self.pc.check_password(passwd)
        self.assertEqual(name, usr)

    def test_Add_Nick(self):
        name = 'Nick'
        passwd = 'mj&6rfE'
        self.pc.add_user(name, passwd)
        usr = self.pc.check_password(passwd)
        self.assertEqual(name, usr)

    @unittest.expectedFailure
    def test_Wrongpass(self):
        passwd = '1111111'
        usr = self.pc.check_password(passwd)

    @unittest.expectedFailure
    def test_RemoveBob(self):
        name = 'Bob'
        passwd = 'uNc1e'
        self.pc.remove_user(name)
        usr = self.pc.check_password(passwd)
        self.assertEqual(name, usr)

    @unittest.expectedFailure
    def test_RemoveAlice(self):
        name = 'Alice'
        passwd = 'C00peR'
        self.pc.remove_user(name)
        usr = self.pc.check_password(passwd)
        self.assertEqual(name, usr)

if __name__ == '__main__':
    unittest.main()