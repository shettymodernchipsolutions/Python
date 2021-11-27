print("----------- Shallow Copy --------------")
lst1 = [[10, 20], [30, 40]]
lst2 = list(lst1)
print("Elements of List 1: ", lst1)
print("Elements of List 2: ", lst2)
print("Identity number of List 1: ", id(lst1))
print("Identity number of List 2: ", id(lst2))
print("Comparison of List 1 & 2: ", lst1 is lst2)
lst1.append([50, 60])
print("Elements of List 1 after appending: ", lst1)
print("Elements in List 2 remains unchanged: ", lst2)
lst1[1][0] = 300
print("Elements in List 1 after modifications: ", lst1)
print("Elements in List 2 after modifications: ", lst2)