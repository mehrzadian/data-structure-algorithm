
def partition(arr, low, high):
    '''partition used in quiksort
    pivot is the last element and all smaller one move to left and bigger 
    to the right of array, in the end pivot will be in it's correct position'''
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  
    return i+1


class sortingAlgorithms:
    def selectionSort(arr):
        for i in range(len(arr)-1):

            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        return arr

    def insertionSort(arr):
        for i in range(1, len(arr)):
            j = i-1
            curr = i
            while arr[curr] < arr[j] and j >= 0:
                arr[curr], arr[j] = arr[j], arr[curr]
                j -= 1
                curr -= 1
        return arr

    # from GeeksForGeeks
    def binarySearch(arr, val, start, end):

        if start == end:
            if arr[start] > val:
                return start
            else:
                return start+1

        if start > end:
            return start

        mid = (start+end)//2
        if arr[mid] < val:
            return sortingAlgorithms.binarySearch(arr, val, mid+1, end)
        elif arr[mid] > val:
            return sortingAlgorithms.binarySearch(arr, val, start, mid-1)
        else:
            return mid

    # from GfG
    def insertionSort(arr):
        for i in range(1, len(arr)):
            val = arr[i]
            j = sortingAlgorithms.binarySearch(arr, val, 0, i-1)
            print(i, "  ", j)
            arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
            print("arr : ", arr)
        return arr

    def quickSort(arr, low, high):
        if low < high:
            i = partition(arr, low, high)

            sortingAlgorithms.quickSort(arr, low, i-1)
            sortingAlgorithms.quickSort(arr, i+1, high)
        return arr

    def mergeSort(arr):
        if len(arr)>1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            sortingAlgorithms.mergeSort(L)
            sortingAlgorithms.mergeSort(R)

            i=j=k=0
            while k<len(arr):
                if j>=len(R) or (i<len(L) and L[i]<=R[j]):
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1
        return arr
            


print(sortingAlgorithms.mergeSort([64, 12, 23, 11, 22]))

def selection_sort(arr):
    for i in range(n:=len(arr)):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print("selection_sort:  ",selection_sort([2,10,32,5,47,85]))

def insertion_sort(arr):
    for i in range(1,n:=len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr
print("insertion_sort:  ",insertion_sort([2,10,32,5,47,85]))

