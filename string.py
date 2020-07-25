myString = "abcdefg"


print(myString)

# slice 3 first
print(myString[:3])

# cut 3 firt
print(myString[3:])

# begin to 2 finish to 5
print(myString[2:5])

#take the 1st and all receive count 4
print(myString[::4])

print(myString.upper())

#******split******
word = "hello world derco"
s = word.split()
print('slit', s)

#******concatenation******
name = "derco"
age = 21

print("***my name is {0} and iam {1} year old".format(name, age))
# print("***my name is %s and iam %d year old" %name %age)

