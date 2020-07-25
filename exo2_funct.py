# #problem 1
# def checkNum(nums):
#     for n in range(len(nums)):
#         if nums[n] == 1 and nums[n+1] == 2 and nums[n+2] ==3:
#             return True
#     return False

# print(checkNum([3,1,2,5,1,2,3,5]))


# #problem 2
# def myWord(mystr):
#     result = ''

#     for s in range(len(mystr)):
#         if s%2 == 0:
#             result = result + mystr[s]
#     return result

# print(myWord('hello'))


# #problem 3
# # def endFunct(mystr2):
# #     mystr2_len = len(mystr2)
# #     if mystr2_len >= 3:
# #         return mystr2.lower()[-3:] == 'abc'

# #     return 'desole mot trop court (-.-)'

# # print(endFunct('zsfAbC'))

# #problem 3 other resolution
# def endFunct2(w1, w2):
#     endW1 = w1[-3:]
#     endW2 = w2[-3:]

#     if endW1 == endW2:
#         print(endW1, '<=>', endW2)
#         return True
#     else:
#         return False
    
# print(endFunct2('abczzz', 'abczzz'))


#problem 4
# def doubleChar(mystr3):
#     mystr3_list = [s*2 for s in mystr3]
#     result = ''

#     for i in range(len(mystr3_list)):
#         result = result + mystr3_list[i]
#     return result

# print(doubleChar('Dk'))

#problem 4 other reslution
def doubleChar(mystr3):
    result = ''
    for s in mystr3:
        result += s*2
    return result

print(doubleChar('Dk'))


#problem 5
# def number_sum(num0):
#     convert_num0 = str(num0)
#     result = 0
#     for i in range(len(convert_num0)):
#         result += int(convert_num0[i])
#     return result

# def num_sum(num1, num2, num3):
#     result = number_sum(num1) + number_sum(num2) + number_sum(num3)
#     return result

# print(num_sum(141,2,1))



