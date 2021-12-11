# print("--------------- Remove -----------------")
#
# lst = [10, 20, 30, 40, 50, 60, 70]
# print("List of all elements: ", lst)
# print("List of 1st element: ", lst[0])
# print("Prints all the list elements: ", lst[::])
# print("List elements of specified range: ", lst[1:5:])
# print("Alternate list elements: ", lst[::2])
# print("Returns empty list: ", lst[-2:-5:])
# print("List of specified range in reverse order: ", lst[-2:-5:-1])
# print("List of all elements in reverse order: ", lst[::-1])
#

x = []

print('Enter the elements? ', end='')

n = int(input())

for i in range(n):
    print('Enter the elements: ', end='')
    x.append(int(input()))

print('The list elements are: ', x)

big = x[0]
small = x[0]

flag = False
for i in range(n - 1):
    for j in range(n - 1 - i):
        if x[j] > x[j + 1]:
            t = x[j]
            x[j] = x[j + 1]
            x[j + 1] = t
            flag = True
    if flag == False:
        break
    else:
        flag = False

print(x)