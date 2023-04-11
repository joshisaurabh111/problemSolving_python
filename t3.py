
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for i,j in zip(list1, list2[::-1]):
#     print(i, j)


#remove empty strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res = list(filter(lambda a: a != '' , list1))
print(res)

list7 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#list7[2][2].insert(2, 7000)
list7[2][2].append(7000)

print (list7)