class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
        
    def open_account(self,name):
        
        if not ( isinstance(name,str) ):
            raise TypeError('invalid input')
        elif isinstance(name,str):
            balance=0
            
            name=BankAccount(name)
           

    """    

    def close_account(self,name):
        if not ( isinstance(name,str) ):
            raise TypeError('invalid input')
        for name in accounts:

    """   
        
    def withdraw_money(self,ammount):
        if not (isinstance(ammount,int) or isinstance(ammount,float)):
            raise TypeError('invalid input type')
        
        if ammount>self.balance:
            raise ValueError('insufficient funds')
        else:
            self.balance-=ammount
            print(self.balance)
        
        
    def deposit_money(self,ammount):
        if not (isinstance(ammount,int) or isinstance(ammount,float)):
            raise TypeError('invalid input type')
        
        self.balance+=ammount
        print(self.balance)

def main():
    customer1=BankAccount()
    customer1.open_account('mbabazi')
    balance_after_deposit=customer1.deposit_money(500000)
    balance_after_withdraw=customer1.withdraw_money(200000)
    

if __name__ == '__main__':
    main()
        
        