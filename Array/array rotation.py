# https://www.geeksforgeeks.org/array-rotation/

# n=int(input())
rotation=int(input())
ls = list(map(int, input().split()))


def rotate():
    ls2 = ls[rotation:]
    for i in range(rotation):
        ls2.append(ls[i])
    print(ls2)


rotate()