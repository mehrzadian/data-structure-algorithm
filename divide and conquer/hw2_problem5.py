# Given a sorted array of distinct integers A[1...n], you want to find out whether there is an index i
# for which A[i] = i. Give a divide and conquer algorithm that runs in O(log n) time to find out an 
# index i if it exists.

def findIndex(arr, inarr):
    if len(arr) > 1:
 
        
        mid = len(arr)//2
 
        L = arr[:mid]
        R = arr[mid:]
 
        findIndex(L, inarr[:mid])
 
        findIndex(R, inarr[mid:])
    else:
        if arr[0] == inarr[0]:
            print(arr[0])
            
arr = list(map(int,input().split()))
inarr= [i for i in range(len(arr))]
findIndex(arr, inarr)
