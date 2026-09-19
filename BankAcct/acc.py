class BankAccount:
    #Bank Name
    bank_name = "AXIS"
    total_bank_accs = 0

    def __init__(self, accname, accno, bal):
        self.accname = accname
        self.accno = accno
        self.bal = bal

        BankAccount.total_bank_accs += 1

    # Depositing money
    def deposit(self, amount):
        self.bal += amount
        print(f"Amount {amount} deposited, Total balance is {self.bal}")

    # Withdrawing money
    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient balance to withdraw")
        else:
            self.bal -= amount
            print(f"Amount {amount} withdrawn, Total balance is {self.bal}")
            
    # Checking balance
    def check_balance(self):
        print("Current Balance is :", self.bal)

    # Display Bank account details
    def display_account_details(self):
        print("Bank Account Details: ")
        print(f"Account holder name: {self.accname}")
        print(f"Account number: {self.accno}")
        print(f"Total balance: {self.bal}")

    @classmethod
    def change_bank(cls, new_bank):
        BankAccount.bank_name = new_bank

ac1 = BankAccount("Raju", 2546532221566, 20000)
ac2 = BankAccount("Rani", 2546532428569, 30000)
ac3 = BankAccount("Rama", 2546532528007, 25000)

ac1.display_account_details()
ac1.deposit(10000)
ac1.withdraw(1000)
ac1.check_balance()

ac2.display_account_details()
ac2.deposit(20000)
ac2.withdraw(2000)
ac2.check_balance()
# Change bank name
ac2.change_bank("ICICI")
print("Bank Account name : ", BankAccount.bank_name)

ac3.display_account_details()
ac3.deposit(10000)
ac3.withdraw(10000)
ac3.check_balance()
# Change bank name
ac3.change_bank("YES")
print("Bank Account name : ", BankAccount.bank_name)

# Dispay the total bank accounts
print("Total bank accounts: ", BankAccount.total_bank_accs)