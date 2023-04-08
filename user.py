class user:
    def __init__(self,username,bal):
        self.name = username
        self.balance = bal

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
            return self
        else:
            self.balance -= amount
            return self

    def display_user_balance(self):
        print("User: "+self.name+", Balance: $"+str(self.balance))
        return self


    def transfer_money(self, other_user, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
            return self
        else:
            self.balance -= amount
            other_user.balance += amount
            print("Transfer succeeds! Now:")
            self.display_user_balance()
            other_user.display_user_balance()
            return self


user1 = user("Xhoni", 1000)
user2 = user("Endi", 10000)
user3 = user("Klea", 10)


user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(350).display_user_balance()

user2.make_deposit(50).make_deposit(10).make_withdrawal(290).make_withdrawal(666).display_user_balance()

user3.make_deposit(10).make_withdrawal(9).make_withdrawal(2).make_withdrawal(4).display_user_balance()

user1.transfer_money(user3,100)