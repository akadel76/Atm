class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = int(balance)

    def balance(self):
        up_balance = int(input(">>>>"))
        self.balance += up_balance

    def withdraw(self):
        minus_balance = int(input(">>>>"))
        if minus_balance > self.balance:
            print("ne pravilno")
        else:
            self.balance -= minus_balance

    def get_balance(self):
        return self.balance


komil = BankAccount(213, "komil", 10000)
komil.withdraw()
print(komil.get_balance())



