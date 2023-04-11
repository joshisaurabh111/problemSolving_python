start = 11
end = 25

list1 = []

for i in range(start, end+1):
    if i % 2 == 0:
        continue
    elif i > 2:
        for j in range(3, i):
            if i % j == 0:
                break
        else:
            list1.append(i)

print(list1)