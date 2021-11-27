#7. Creating class about mobiles

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def specifications(self):
        print("Specifications of mobile: ", self.brand, self.model, self.price)

Specification = Mobile("Oneplus", "Oneplus 7", 30000)
Specification.specifications()
