#13. Creating class about humans physique.

class Physique:
    #state
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    #behaviour
    def bmi(self):
        print("Height and weight of: ", self.name, self.age, self.height, self.weight)

characteristics = Physique("Gowtham", "27", " 5'10'' ", "75 kg")
characteristics.bmi()