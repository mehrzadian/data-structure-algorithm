def rec1(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    return rec1(n-1)+rec1(n-2)*2

def rec2(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    return rec2(n-1)+rec2(n-2)*2 - rec2(n-3)
print(rec2(10))