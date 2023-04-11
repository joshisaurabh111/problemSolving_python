str = 'afgkfgkgkaf'

s1 = 'gk'

count = str.count(s1)
print (count)

res = [i for i in range(len(str)) if str.startswith(s1, i)]
print(res)

i=[]
for x in range(len(str)):
    if str.startswith(s1, x):
        i.append(x)

print (i)