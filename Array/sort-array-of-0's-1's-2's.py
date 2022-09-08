# Given an array containing only 0’s, 1’s, and 2’s, sort it in linear time and using constant space.
def sort(ls):
    ones=0
    zeros=0
    twos=0
    for x in ls:
        if x==0:
            zeros+=1
        elif x==1:
            ones+=1
        else:
            twos+=1
    return [0]*zeros+[1]*ones+[2]*twos
print(sort(ls:=[1,1,2,1,0,0,1,2,2,0]))
#threeWayPartioning
def swap(ls,a,b):
    temp=ls[a]
    ls[a]=ls[b]
    ls[b]=temp
def pivotSort(ls):
    start=mid=0
    end=len(ls)-1
    pivot = 1
    while mid<=end:
        if ls[mid]<pivot:
            swap(ls,start,mid)
            start+=1
            mid+=1
        elif ls[mid]>pivot:
            swap(ls,end,mid)
            end-=1
        else:
            mid+=1
print(sort(ls))