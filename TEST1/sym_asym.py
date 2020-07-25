def icore(data):
    for i in range(0, len(data)//2):
        if data[i] != data[len(data)-1-i]:
            return -1
        else:
            return 0

print(icore([1,2,2,2]))



#pour comprendre

# def icore(data):

#     for i in range(0, len(data)//2):
#         print("moitier du tab",data[i])
#         print("autre",data[len(data)-1-i])

# print(icore([1,2,3,4]))