# 2. Creating the class of employee

class Employee:
    #state
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary
    #behaviour
    def get_emp_details(self):
        print("Employee Details: ", self.eid, self.name, self.salary)

det = Employee("MCS-0039", "Katta Satish Babu", 90000)
det.get_emp_details()