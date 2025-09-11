import copy

list1 = [[1, 2], [3, 4]]
# list2 = copy.copy(list1)
list2 = copy.deepcopy(list1)


list2[0][0] = 99

print("list1:", list1)  # [[99, 2], [3, 4]]
print("list2:", list2)  # [[99, 2], [3, 4]]
