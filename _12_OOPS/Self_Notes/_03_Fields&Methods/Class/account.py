#4. Creating class of Account Holder

class AccountHolder:

    def __init__(self):
        self.bal = 10000

    def get_bal(self):
        return self.bal

    def set_bal(self,amt):
        if amt > 0:
            self.bal = amt
        else:
            print("Invalid amount")

ah = AccountHolder()
print("Initial Balance is: ", ah.get_bal())
ah.set_bal(20000)
print("Current Balance is: ", ah.get_bal())
