# bank class

class Bank:
    def __init__(self, acc, bal):
        self.acc = acc
        self.bal = bal

    def deposit(self, amt):
        self.bal = self.bal + amt

    def withdraw(self, amt):
        self.bal = self.bal - amt

    def show(self):
        print("balance:", self.bal)


b1 = Bank(101, 5000)

b1.deposit(1000)
b1.withdraw(500)

b1.show()