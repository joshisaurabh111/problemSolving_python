# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}

# d1 = dict.fromkeys(employees)
# for k,v in d1.items():
#     d1[k] = defaults

# print(d1)

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys = ["name", "salary"]

# d2 = {}
# for k in keys:
#     d2[k] = sampleDict.get(k)
    
# print(d2)

for k in keys:
    sampleDict.pop(k)

print(sampleDict)