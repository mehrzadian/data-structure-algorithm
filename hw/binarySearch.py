n = int(input())
ls = list()
for i in range(n):
    ls.append(int(input()))
data = int(input())


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


print(binarySearch(data, ls))
