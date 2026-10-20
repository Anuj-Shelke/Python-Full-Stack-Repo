class BankAccount():
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number 
        self.balance = balance 

    def deposit(self,amount):
        
        self.balance += amount
        print("Updated balance is : ",self.balance)

    def withdraw(self,amount):
    
        if(amount > self.balance):
            print("Insufficient Balance : ",self.balance)
        else:
            self.balance = self.balance-amount

    def display(self):
        print("Name : ",self.name)
        print("Account Number : ",self.account_number)
        print("Balance : ",self.balance)

A1 = BankAccount("Anuj","ACC101",10000)
A2 = BankAccount("Rahul ","ACC102",20000)





    