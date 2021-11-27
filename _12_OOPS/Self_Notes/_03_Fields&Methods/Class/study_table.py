#10. Creating class of Study table

class Table:
    #state
    def __init__(self, brand, country, length, breadth, height, price):
        self.brand = brand
        self.country = country
        self.length = length
        self.breadth = breadth
        self.height = height
        self.price = price

    #behaviour
    def study_table(self):
        print("Table specifications: ",self.brand, self.country, self.length, self.breadth, self.height, self.price)

Study_table = Table("Graham Study Table", "INDIA", 760,  1199,  599, 5999)
Study_table.study_table()
