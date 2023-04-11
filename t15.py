inp = [['p1:a' ,'p3:b' ,'p5:x'],['p1:b', 'p2:q', 'p5:x']]
temp_dict = {}


for l1 in inp:
    for ele in l1:
        key , value = ele.split(':')
        temp_dict[key] = value

print (temp_dict)