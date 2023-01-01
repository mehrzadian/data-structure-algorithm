import math
n = int(input("len of list: "))
ls = list()
for i in range(n):
    ls.append(int(input()))
data = int(input("the data you are looking for? "))

def linearSearch(data,ls):
    for i in range(len(ls)):
        if ls[i]==data:
            return i
    return 'not in the list!'

def binarySearch(data, ls=[]):
    if len(ls) == 1:

        return ls[0]
    else:
        ls.sort()
        medium = ls[len(ls) // 2]
        if data > medium:
            binarySearch(data, ls[medium:])
        elif data < medium:
            binarySearch(data, ls[:medium])
        return ls.index(medium)




def jumpSearch(data, ls = []):
    ls.sort()
    jumpingBlock =  int(math.sqrt(n))
    for i in range(0,len(ls),jumpingBlock):
        if ls[i]== data:
            return i
        elif ls[i]> data:
            linearSearch(data, ls[i-jumpingBlock:i])
            return
    return 'not in the list'

print(jumpSearch(data, ls))