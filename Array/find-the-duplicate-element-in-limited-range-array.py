def findDuplicate(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[j]==ls[i]:
                print('the duplcate is: ',ls[i])
                return
def findDup(ls):
    d={}

    for i, e in enumerate(ls):
        d[e]=i
    print(d)
    compLs=[i for i in range(len(ls))]
    print(compLs)
    for key, value in d.items():
        compLs.remove(value)
    if compLs.__len__()!=0:
        print('the duplicate is: ',ls[compLs[0]])
findDup([1,100,100,3,4,5,6])
