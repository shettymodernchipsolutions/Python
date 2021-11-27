#1. Creating the class for laptop
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model  = model
        self.price = price

    def get_prodInfo(self):
        print("Product details are: ", self.brand, self.model, self.price)

details = Laptop("Realme", "Realme Notebook", 59999)
details.get_prodInfo()
