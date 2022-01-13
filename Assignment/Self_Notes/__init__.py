def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)

        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1


# num = int(input('Enter the number of elements in the list: '))
list1 = [i.replace(' ', '') for i in f"{input('Enter the list : ')}".split(' ')]
list1 = [int(i) for i in list1 if i.isdigit()]
mergesort(list1)
print('Sorted list are: ', list1)
