#Fernandez Girlly
class BankAccount:

    def __init__(self, balance):
        self.__balance_gmf = balance

    def deposit(self, amount):
        self.__balance_gmf += amount

    def withdraw(self, amount):

        if amount <= self.__balance_gmf:
            self.__balance_gmf -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance_gmf

account_gmf = BankAccount(5000)

account_gmf.deposit(1000)
account_gmf.withdraw(2000)

print("Balance:", account_gmf.get_balance())