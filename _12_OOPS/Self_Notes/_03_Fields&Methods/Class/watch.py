#11. Creating class of a watch

class Watch:
    #state
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    #behaviour
    def details(self):
        print("Details of the watch: ", self.brand, self.model, self.price, self.color)

Specifications = Watch("Rolex", "1987 pre-owned Cosmograph Daytona 40mm", "Rs.2,27,11,709", "Yellow Gold")
Specifications.details()
