class BankAccount:
    def __init__(self, account_holder_name, balance):
        self.account_holder_name = account_holder_name
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal amount cannot be greater than Account Balance")
        elif amount <= 0:
            print("Withdrawal amount should be greater than 0")
        else:
            self.__balance -= amount
            print(f"Rs. {amount} has been withdraw from the account successfully")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be greater than 0")
        else:
            self.__balance += amount
            print(f"Rs. {amount} has been deposit to the account successfully")

    @property
    def balance(self):
        return self.__balance


my_account = BankAccount("Naman", 100000)
print(my_account.balance)
my_account.withdraw(1000000)
my_account.withdraw(10000)
print(my_account.balance)
