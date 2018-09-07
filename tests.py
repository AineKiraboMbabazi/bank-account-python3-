import unittest

from Accounts import BankAccount

class testAccount(unittest.TestCase):
    def test_name_type(self):
        self.assertRaises(TypeError, BankAccount.open_account,[1,2,3])

    @unittest.skip (" work in progress ")
    def test_ammount(self):
        self.assertRaises(ValueError,BankAccount.withdraw_money,'hello')
        self.assertRaises(TypeError,BankAccount.withdraw_money,0)
        self.assertRaises(ValueError,BankAccount.deposit_money,'hello')
        self.assertRaises(TypeError,BankAccount.deposit_money,0)


if __name__=='__main__':
    unittest.main()