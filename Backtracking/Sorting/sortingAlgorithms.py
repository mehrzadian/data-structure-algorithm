class sortingAlgorithms:
    def selectionSort(arr):
        for i in range(len(arr)-1):
            
            for j in range(i,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j]= arr[j],arr[i]
            
        return arr

    def insertionSort(arr):
        for i in range(1,len(arr)):
            j=i-1
            curr = i
            while arr[curr]<arr[j] and j>=0:
                arr[curr],arr[j] = arr[j],arr[curr]
                j-=1
                curr-=1
        return arr
print(sortingAlgorithms.insertionSort([64,12,23,11,22]))
