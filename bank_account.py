# Fernandez,Girlly
class BankAccount:

    def __init__(self, account_name, balance):
        self.account_name_gmf = account_name
        self.balance_gmf = balance

    def deposit(self, amount):
        self.balance_gmf += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance_gmf:
            self.balance_gmf -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance_gmf)

account_gmf = BankAccount("Juan", 5000)

account_gmf.deposit(1000)
account_gmf.withdraw(2000)
account_gmf.display_balance()