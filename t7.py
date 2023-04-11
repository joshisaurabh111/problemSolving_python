# sampleDict = {'a': 100, 'b': 200, 'c': 300}

# if 400 in sampleDict.values():
#     print(True)
# else:
#     print(False)

# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sampleDict['location'] = sampleDict.pop('city')
# print(sampleDict)


# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# res = max(sampleDict, key=sampleDict.get)
# print(res)

l1 = [3,4,3,4,5]
d1 = {}
for i in l1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

res = min(d1, key=d1.get)
print(res)