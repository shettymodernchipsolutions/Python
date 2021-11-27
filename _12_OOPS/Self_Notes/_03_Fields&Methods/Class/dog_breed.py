#6. Creating class of a dog

class Dog:
    def __init__(self, breed, color, price):
        self.breed = breed
        self.color = color
        self.price = price

    def breed_details(self):
        print("Information of dogs: ", self.breed, self.color, self.price)

details = Dog("Dashhund", "Black", 8000)
details.breed_details()
