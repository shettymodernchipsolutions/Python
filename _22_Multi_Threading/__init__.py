# class Employee_A:
#
#     def __init__(self, emp_data):
#         self.emp_data = emp_data
#         self.dict1_list = []
#         for list1 in emp_data.values():
#             for dict_emp in list1:
#                 self.dict1_list.append(dict_emp)
#
#                 # prints even id's
#
#     def even_id(self):
#         for dict1 in self.dict1_list:
#             if dict1['eid'] % 2 == 0:
#                 print('---------employees with even id -------------\n')
#                 print(dict1['name'], dict1['eid'], '\n')
#
#     # return only name and salary
#     def emp_salary(self):
#         print('---------employee total salary ------------\n')
#         for dict1 in self.dict1_list:
#             dict1['salary'] = sum(dict1['salary'].values())
#             print(dict1['name'], ' : ', dict1['salary'], '\n')
#
#     # return all the detials
#     def emp_details(self):
#         print('--------employee details----------')
#         for dict1 in self.dict1_list:
#             for key in dict1:
#                 print(key, ' : ', dict1[key], '\n')
#
#             print('-' * 30)
#
#
# class Employee_B(Employee_A):
#
#     # prints the emp detials whose salary greater than 10000
#     def salary_greater(self):
#         print('\n---------employees with salary greater than 10000---------\n')
#         for dict1 in self.dict1_list:
#             if dict1['salary'] > 10000:
#                 print(dict1['name'], ' : ', dict1['salary'])
#
#     # return all the details
#     def details(self):
#         super().emp_details()
#
#     # return name and total salary
#     def salary(self):
#         super().emp_salary()
#
#     # return the location according to the id
#     def location(self):
#         print('-----------location of employees-----------------')
#         for dict1 in self.dict1_list:
#             print(dict1['eid'], dict1['name'], ' : ', dict1['location'])
#
#
# emp_A = {'A': [{'eid': 100, 'name': 'mike', 'salary': {'BA': 100, 'HR': 2000, 'SA': 300}},
#                {'eid': 101, 'name': 'john', 'salary': {'BA': 22200, 'HR': 6000, 'SA': 100}}]}
#
# emp_B = {'B': [{'eid': 100, 'name': 'mike', 'salary': {'BA': 400, 'HR': 1000, 'SA': 400}, 'location': 'HYD'},
#                {'eid': 101, 'name': 'john', 'salary': {'BA': 34200, 'HR': 5000, 'SA': 300}, 'location': 'Delhi'}]}
#
# obj_A = Employee_A(emp_A)
# obj_A.even_id()
# obj_A.emp_salary()
# obj_A.emp_details()
#
# obj_B = Employee_B(emp_B)
# obj_B.salary()
# obj_B.salary_greater()
# obj_B.details()
# obj_B.location()


def prime(n):
    x = True
    for i in range(2, n):
        if n % i == 0:
            x = False
            break
        else:
            x = True
    return x


# num = int(input('Enter the number: '))

# i = 2
# c = 1

# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#
#     if c > num:
#         break

for i in range(171,201):
    if prime(i) == True:
        print(i)


