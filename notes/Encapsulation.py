class Bank:
    def __init__(self, owner, balance):
        self.owner = owner             
        self.__balance = balance        
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount!")

account = Bank("Jackson", 1000)
print(account.get_balance())
account.set_balance(2000)
print(account.get_balance())