print('starts:')
start = list(map(int, input().split()))
print('ends:')
end = list(map(int, input().split()))
n= len(start)
# sort by end time
def insertionSort(start, end):
        for i in range(1, len(end)):
            j = i-1
            curr = i
            while end[curr] < end[j] and j >= 0:
                end[curr], end[j] = end[j], end[curr]
                start[curr], start[j] = start[j], start[curr]
                j -= 1
                curr -= 1
        return start,end

#activitySelection
def activitySelection(start, end):
    s = insertionSort(start, end)
    start, end = s[0], s[1]
    selected=[]
    selected.append(end[0])
    x=0
    
    for i in range(1,len(end)):
        if start[i] > selected[x]:
            selected.append(end[i])
            x+=1
    return selected
print(activitySelection(start, end))
