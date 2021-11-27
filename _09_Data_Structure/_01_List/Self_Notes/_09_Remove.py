print("-------------- Remove ------------------")
lst = [10, 20, 30, 40, 50, 60]
print("Before removal: ", lst)
lst.remove(30)
print("After removal: ", lst)

lst = [10, 20, 30, 40, 50, 30]
print("Before removal: ", lst)
lst.remove(30)
print("After removal: ", lst)

lst = [10, 20, 30, 40, 50, 30]
print(30 in lst)
print(30 not in lst)

lst = [10, 20, 30, 40, 50, 30]
print("Before iteration: ", lst)

while 30 in lst:
    lst.remove(30)
print("After iteration: ", lst)
