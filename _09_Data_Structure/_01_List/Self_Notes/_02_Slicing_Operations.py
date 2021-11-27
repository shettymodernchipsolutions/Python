print("--------------------------- Slicing ----------------------------")
# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[1:4] = 99
# print(lst)

lst1 = [10, 20, 30, 40, 50]
print("List of all elements: ", lst1)
lst1[1:4] = [99]
print("After slicing elements from index 1-4: ", lst1)

lst2 = [10, 20, 30, 40, 50]
print("List of all elements: ", lst2)
lst2[1:4] = [99, 88, 77]
print("After replacing all the elements from 1-4: ", lst2)

lst3 = [10, 20, 30, 40, 50]
print("List of all elements: ",lst3)
lst3[1:4] = [99, 88, 77, 66]
print("We are adding additional elements after replacing elements from 1-2: ", lst3)

lst4 = [10, 20, 30, 40, 50]
print("List of all elements: ", lst4)
lst4[::2] = [99, 99, 99]
print("Replacing a single value in alternate index no.: ",lst4)
