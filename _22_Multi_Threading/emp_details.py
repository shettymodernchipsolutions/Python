emp_A = {'A': [
    {'eid': 100, 'name': 'mike', 'salary': {'BA': 100, 'HR': 2000, 'SA': 300}},
    {'eid': 101, 'name': 'john', 'salary': {'BA': 22200, 'HR': 6000, 'SA': 100}}],
        'B': [
            {'eid': 300, 'name': 'mike', 'salary': {'BA': 400, 'HR': 1000, 'SA': 400}, 'location': 'HYD'},
               {'eid': 301, 'name': 'john', 'salary': {'BA': 34200, 'HR': 5000, 'SA': 300}, 'location': 'Delhi'}
            ]
        }

emp_B = {'B': [{'eid': 100, 'name': 'mike', 'salary': {'BA': 400, 'HR': 1000, 'SA': 400}, 'location': 'HYD'},
               {'eid': 101, 'name': 'john', 'salary': {'BA': 34200, 'HR': 5000, 'SA': 300}, 'location': 'Delhi'}]}

class emp:
    def __init__(self,one_emp):
        for one_attr in one_emp.keys():
            setattr(self, one_attr, one_emp[one_attr])


    def print_one_emp(self):
            print("---------------printing one emp---------------")
            print("EID = ",self.eid)
            print("NAME = ",self.name)
            #print("SALARY = ",self.salary)

    def print_salary(self):
        self.net = 0
        for one_allowance in self.salary.values():
            self.net += one_allowance
        print("EMP : ",self.name," has net salary of ",self.net)

class A:
    def __init__(self, emp_A):
        self.emp_list = []
        for class_name in emp_A.keys():
            if(self.__class__.__name__ == class_name):
                for full_lists in emp_A.values():
                    for one_emp in full_lists:
                        if(one_emp["eid"] %2 == 0):
                            k = emp(one_emp)
                            k.print_one_emp()
                            k.print_salary()


    #def show_emp(self):
     #   for e in self.emp_list:
      #      print(e)

objA = A(emp_A)
#objA.show_emp()
