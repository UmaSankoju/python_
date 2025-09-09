class BankAccount:
    def __init__(self, user_account, balance, pin):
        self.user_account = user_account      
        self._balance = balance                   
        self.__pin = pin                          

    def deposit_money(self, amount):
        if amount > 0:
            self._balance += amount
            print("you deposited",amount)
        else:
            print("you Deposited Nothing")

  
    def withdraw_money(self, amount, pin):
        if pin != self.__pin:
            print("you entered Wrong pin")
        elif amount > self._balance:
            print("you dont't have suffitient Amount to withdraw")
        else:
            print("you withdrawed",amount)


    def __str__(self):
        return f"Account Holder: {self.user_account}\n Balance: {self._balance}"

   
    def __add__(self, other):
        return self._balance + other._balance

acc1 = BankAccount("jane doe", 15000, 1234)
acc2 = BankAccount("john doe", 20700, 5678)

print(acc1)   
print(acc2)

acc1.deposit_money(500)
acc1.withdraw_money(3000, 1234)   
acc2.withdraw_money(10050, 9999)   


total_balance = acc1 + acc2   
print("Combined Balance of acc1 and acc2:", total_balance)
