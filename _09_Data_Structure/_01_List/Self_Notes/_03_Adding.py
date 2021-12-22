# print("--------------------------- Adding ----------------------------")
# lst = [10, 20, 30, 40, 50]
# print("List of all elements: ", lst)
# lst.append(60)
# print("After appending: ", lst)
# lst.append([70, 80, 90])
# print("After entering the list in append method : ", lst)
# lst = [10, 20, 30, 40, 50]
# lst = lst + [70, 80, 90]
# print("After concatenating two lists: ", lst)
#
# lst = [10, 20, 30, 40, 50]
# print("List of all elements: ", lst)
# lst.append([70, 80, 90])
# print("We can add multiple elements if we declare list using append", lst)
#
# lst = [10, 20, 30, 40, 50]
# print("List of all elements: ", lst)
# lst.append(60)
# print("After append: ", lst)
# lst = lst + [70, 80, 90]
# print("Concatenating the list: ", lst)
#
# lst = [10, 20, 30, 40, 50]
# print("List of all elements: ", lst)
# lst.append(60)
# print("Using append: ", lst)
# lst.extend([70, 80, 90])
# print("List after extending elements", lst)
#
# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst.insert(2, 99)
# print(lst)


from itertools import product
n, m = [int(x) for x in input().split()]

l1 = list()

for i in range(n):
    l = list(map(int, input().split()))[1:]
    l1.append(l)

r = map(lambda x : sum(i * i for i in x) % m, product(*l1))
print(max(r))