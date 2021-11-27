#12. Creating class of a Fridge

class Fridge:
    #state
    def __init__(self, brand, model, color, price, form_factor, pattern):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.form_factor = form_factor
        self.pattern = pattern

    #behaviour
    def info(self):
        print("Specification of the fridge: ", self.brand, self.model, self.color, self.price, self.form_factor, self.pattern)

Details = Fridge("Whirlpool", "INTELLIFRESH INV CNV 278 3S", "Black", "₹26,490.00", "Standard_double_door", "Solid")
Details.info()