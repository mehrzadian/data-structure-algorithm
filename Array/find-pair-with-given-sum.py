
def findPair(ls,target):
    tuparr = []
    for i in range(len(ls)):
        first = ls[i]
        for j in range(i+1,len(ls)):
            second = ls[j]
            if first+ second == target:
                tup = (first,second)
                tuparr.append(tup)
    if tuparr.__len__()==0:
        print('pair not found')
        return ''
    for i in range(len(tuparr)):
        print('pair found: ',tuparr[i])
        if len(tuparr)>i+1:
            print('or')
    return ''
nums = [8, 7, 2, 5, 3, 1]
target = 10
findPair(nums,target)
nums = [5, 2, 6, 8, 1, 9]
target = 12
findPair(nums,target)

# sort first then find pair
