#3. Create class of a Car

class Car():
    #states of object
    def __init__(self):
        self.brand = 'BMW'
        self.cc = 2100
        self.color = 'blue'

    #behaviours of object
    def start_engine(self):
        print("Engine is starting")

    def shift_gear(self):
        print("shifting the gear")

    def accelerate(self):
        print("car is accelerating")

def main():
    c1 = Car()
    print(c1.brand)
    print(c1.cc)
    print(c1.color)
    c1.start_engine()
    c1.shift_gear()
    c1.accelerate()

if __name__ == '__main__':
    main()