
    
print( 'names')
names = list(input().split())
print('deadlines')
deadlines = list(map(int,input().split()))
print('profits')
profits = list(map(int,input().split()))
jobs = []
for i in range(len(names)):
    jobs.append([names[i],deadlines[i],profits[i]])
    
print(jobs)

jobs = sorted(jobs, key= lambda x:x[2], reverse=True)
#maximum deadline
max=0
for i in range(len(jobs)):
    if max < jobs[i][1]:
        max = jobs[i][1]

#greedy approach
sj=[0]*max
for i in range(len(jobs)):
    for j in range(jobs[i][1],0,-1):
        if sj[j-1] == 0:
            sj[j-1] = jobs[i][0]
            break
print(*[i for i in sj if i != 0])

    

