
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

    #from GeeksForGeeks
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
  
    #from GfG
    def insertionSort(arr):
        for i in range(1, len(arr)):
            val = arr[i]
            j = sortingAlgorithms.binarySearch(arr, val, 0, i-1)
            print(i,"  ",j)
            arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
            print("arr : ", arr)
        return arr
  
  


        
print(sortingAlgorithms.insertionSort([64,12,23,11,22]))
