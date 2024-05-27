class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# إنشاء نموذج BankAccount
account = BankAccount("123456789", "John Doe")

# إيداع $1000
account.deposit(1000)
print("Current balance after deposit: $", account.get_balance())

# سحب $500
account.withdraw(500)
print("Current balance after withdrawal: $", account.get_balance())
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

    def print(self):
        print("Current balance: $", self.get_balance())
        print("Interest rate: ", self.interest_rate)

# إنشاء نموذج SavingsAccount
savings_account = SavingsAccount("987654321", "Jane Smith", 0.05)  # سعر الفائدة 5%

# تطبيق الفائدة
savings_account.apply_interest()

# طباعة الرصيد الحالي وسعر الفائدة
savings_account.print()
