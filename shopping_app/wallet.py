class Wallet:
    from ownable import set_owner

    def __init__(self, owner):
        self.set_owner(owner)
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount

    def decrease_balance(self, amount):
        if not self.balance >= amount:
            print("残高が不足しています。")
            return
        self.balance -= amount
