# n, k, q = int(input()), int(input()), int(input())
ls = list()


# for i in range(n):
#     ls.append(int(input()))


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


def select(ls, q=3, k=0):
    print(ls)
    if ls.__len__() == 0:
        return
    ls2 = list()
    newls = list()
    chunks = [ls[x:x + q] for x in range(0, len(ls), q)]
    for i in range(chunks.__len__()):
        bubbleSort(chunks[i])
    medium = list()
    for chunk in chunks:
        medium.append(chunk[chunk.__len__() // 2])
    bubbleSort(medium)
    print("hhhhhh ", chunks)
    if medium.__len__() % 2 == 0:
        md = medium[(medium.__len__() // 2) - 1]
    else:
        md = medium[(len(medium) // 2)]
    s1, s2, s3 = list(), list(), list()
    for i in ls:
        if i < md:
            s1.append(i)
        elif i == md:
            s2.append(i)
        else:
            s3.append(i)
    print(s1, "    ", s2, "   ", s3)
    print("md: ", md)

    n1, n2, n3 = len(s1), len(s2), len(s3)
    print(n1, "    ", n2, "   ", n3)
    if k < n1:
        print("k: ", k)
        select(s1, q, k)
    elif k == n2 + n1:
        if len(s2) >= k:
            return s2[k]
    else:
        print("k: ", k)
        select(s3, q, k - n1 - n2)
    print(medium)


ls = [6, 11, 18, 10, 8, 7, 15, 17, 45, 22, 32, 37, 40, 54, 43, 38, 28, 27]
print(select(ls, 5, 10))
# print(select([1, 2, 3, 88, 5, 6, 7, 0, 9, 10], 3, 2))
