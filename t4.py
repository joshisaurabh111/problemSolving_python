# # list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # l1 = ['h', 'i', 'j']

# # for ele in l1:
# #     list1[2][1][2].append(ele)

# # print (list1)

# list1 = [5, 10, 15, 20, 25, 50, 20]

# # for ind, val in enumerate(list1):
# #     if val == 20:
# #         list1[ind] = 200
# #         break

# # print(list1)

# index = list1.index(20)
# list1[index]

import copy

list1 = [5, 20, 15, 20, 25, 50, 20]

# print(list1)

str = "SOURABH"
test = str.split() 
print(test)

list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
list1.append(100)

print(list2, list3)