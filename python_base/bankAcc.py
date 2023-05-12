class Bank_acc:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def getId(self):
        return self.id

    def setId(self, val):
        self.id = val

    def getName(self):
        return self.name

    def setName(self, val):
        self.name = val

    def getBalance(self):
        return self.balance

    def setBalance(self, val):
        self.balance = val

    def deposit(self):
        deposit = float(input('Diposit value: '))
        self.balance += deposit

    def drow_money(self):
        drow_money = float(input('Drow value: '))
        self.balance -= drow_money


a = Bank_acc(1, "Boris Isac", 'Pobre')
print(a.__dict__)
b = Bank_acc(2,"Pai Natal", 5.99)
print(b.__dict__)
b.deposit()
b.drow_money()
print(b.getBalance())