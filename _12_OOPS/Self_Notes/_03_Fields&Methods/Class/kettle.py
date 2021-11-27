# 15. Creating class of a kettle.

class Kettle:

    def __init__(self,brand, colour, capacity, material, wattage):
        self.brand = brand
        self.colour = colour
        self.capacity = capacity
        self.material = material
        self.wattage = wattage

    def info(self):
        print("Details about the kettle: ",self.brand, self.colour, self.capacity, self.material, self.wattage)

details = Kettle("IBELL", "White", "2 litres", "Stainless Steel", "1500 Watts")
details.info()