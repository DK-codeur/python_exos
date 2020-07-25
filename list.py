mylist = [1, 2, 3, 'a', 'b', 'c']

print(len(mylist))

print(mylist[4:])
print(mylist[:4])

mylist[0] = "new item"
print(mylist)

#print(dir(mylist))

matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

sec_pos = [ pos[1] for pos in matrix ]
print(sec_pos)