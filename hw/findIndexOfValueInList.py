n = int(input())

ls = list()
for i in range(n):
    ls.append(int(input()))
x = int(input("What value are you searching for? "))
# print(ls.index(x))

def index(ls,x):
    a=0
    isThere=-1
    for num in ls:
        if num==x:
            print(a)
            isThere=0
        a+=1
    print(isThere if isThere==-1 else '',end='')
index(ls,x)