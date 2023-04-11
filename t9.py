text = 'this is sourabh joshi sourabh joshi'

input1  = text.split(' ')

#print(input1)
d1 = {}
for ind in range(len(input1)-1):
	if (input1[ind], input1[ind+1]) in d1:
		d1[(input1[ind], input1[ind+1])] += 1
	else:
		d1[(input1[ind], input1[ind+1])] = 1

print(sorted(d1.items(),key=lambda x:x[1] ,reverse=True)[:2])


# d2 = {}
# # d1 -- is the dictionary name
# d2 = sorted(d1.items, key = d1.get, reverse=True)
# print(d2)

