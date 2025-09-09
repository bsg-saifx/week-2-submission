class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    
    def deposit(self, money):
        self.balance+=money
        print(f"New Balance: {self.balance}")
        return self.deposit
    
    def is_empty(self):
        return self.balance<=0

    def withdraw(self,withdraw):
        if self.is_empty():
            print("you are broke")
        elif withdraw>self.balance:
            print("You don't have sufficient balance")
        else:
            self.balance-=withdraw
            print(f"Remaining Balance: {self.balance}")
        return self.balance

    def balance_state(self):
        print(f"Your Balance: {self.balance}")


Acc = BankAccount()
Acc.deposit(1000)
Acc.withdraw(500)
Acc.withdraw(600)
Acc.deposit(1000)
Acc.balance_state()
Acc.withdraw(800)
