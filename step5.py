class BankAccount:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Деньги внесены, текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Деньги сняты, текущий баланс: {self.balance}")
        else:
            print("Недостаточно средств на счете")


    account = BankAccount("John Doe", 100)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)
    print(f"Текущий баланс: {account.balance}")
