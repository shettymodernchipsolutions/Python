#5. Creating class of a Student academics

class Student:
    def __init__(self, reg_no, name, percent):
        self.reg_no = reg_no
        self.name = name
        self.percent = percent

    def get_stuInfo(self):
        print("Student details: ", self.reg_no, self.name, self.percent)

details = Student(120909775, "Shamanth", 78)
details.get_stuInfo()