class Account:
    def __init__(self, accno, name, acctype, accbal):
        self.__accno = accno
        self.__name = name
        self.__acctype = acctype
        self.__accbal = accbal

    @property
    def accno(self):
        return self.__accno

    @accno.setter
    def accno(self, accno):
        self.__accno = accno

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def acctype(self):
        return self.__acctype

    @acctype.setter
    def acctype(self, acctype):
        self.__acctype = acctype

    @property
    def accbal(self):
        return self.__accbal

    @accbal.setter
    def accbal(self, accbal):
        self.__accbal = accbal

    def deposit(self, amount):
        self.__accbal += amount
        print("Amount deposited successfully")
        print("Current Balance:", self.__accbal)

    def withdraw(self, amount):
        if amount <= self.__accbal:
            self.__accbal -= amount
            print("Amount withdrawn successfully")
            print("Current Balance:", self.__accbal)
        else:
            print("Insufficient balance")


lstaaccount = []

while True:
    print("\n1. Create Account")
    print("2. Display Accounts")
    print("3. Search Account")
    print("4. Deposit")
    print("5. Withdrawal")
    print("6. Exit")

    Ch = int(input("Enter your choice: "))

    if Ch == 1:
        A_no = int(input("Enter your account number: "))
        C_name = input("Enter your name: ")
        A_type = input("Enter your account type: ")
        A_bal = int(input("Enter your balance: "))

        accobj = Account(A_no, C_name, A_type, A_bal)
        lstaaccount.append(accobj)

        print("Account created successfully")

    elif Ch == 2:
        if len(lstaaccount) == 0:
            print("No accounts available")
        else:
            for a in lstaaccount:
                print("\nAccount Number:", a.accno)
                print("Customer Name:", a.name)
                print("Account Type:", a.acctype)
                print("Account Balance:", a.accbal)

    elif Ch == 3:
        A_no = int(input("Enter account number to search: "))

        found = False

        for a in lstaaccount:
            if a.accno == A_no:
                print("Account Number:", a.accno)
                print("Customer Name:", a.name)
                print("Account Type:", a.acctype)
                print("Account Balance:", a.accbal)
                found = True
                break

        if found == False:
            print("Account not found")

    elif Ch == 4:
        A_no = int(input("Enter account number: "))

        for a in lstaaccount:
            if a.accno == A_no:
                amount = int(input("Enter amount to deposit: "))
                a.deposit(amount)
                break
        else:
            print("Account not found")

    elif Ch == 5:
        A_no = int(input("Enter account number: "))

        for a in lstaaccount:
            if a.accno == A_no:
                amount = int(input("Enter amount to withdraw: "))
                a.withdraw(amount)
                break
        else:
            print("Account not found")

    elif Ch == 6:
        print("Thank you")
        break

    else:
        print("Invalid choice")