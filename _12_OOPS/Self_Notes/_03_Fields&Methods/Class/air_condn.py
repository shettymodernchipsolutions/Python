#9. Creating class of a Air Conditioner

class AC:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def details(self):
        print("Air conditioner of: ", self.brand, self.model, self.price)

query = AC("Life's Good", "LG 1 Ton 5 Star LS-Q12MNZA Inverter Split AC", 37990)
query.details()