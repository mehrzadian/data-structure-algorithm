import datetime
import time

x, n = list(map(int,input().split()))
st=datetime.datetime.now()
print(10//8)
#naive approach
# space :O(1)
# time: O(n)
def naivePow(x,n):
    d = x
    for i in range(n-1):
        x*=d
    return x
#recursive approach
# space comp = O(n)
# time = O(n)
def recPow(x,n,d):

    if n==1:
        return x
    if n == 0 :
        return 1
    return recPow(x*d,n-1,d)
print(naivePow(x,n))
print(recPow(x,n,x))

# divide and conquer approach
# space: O(logn)
# time: O(logn)
def divConPow(x,n):
    temp =0
    if n==1:
        return x
    if n==0:
        return 1
    temp =  ddivConPow(x, n//2)
    return  temp* temp if n%2==0 else (x*temp) * temp
    
et = datetime.datetime.now()
tim = et - st
print(divConPow(x,n))
print(tim)