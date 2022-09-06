def findDuplicate(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[j]==ls[i]:
                print('the duplcate is: ',ls[i])
                return
