def findSub(ls):
    for i in range(len(ls)):
        x=ls[i]
        xsub=[x]
        # print()
        if x==0:
            print(xsub)
        for j, e in enumerate(ls[i+1:]):
            xsub.append(e)
            x+=e
            # print('x: ',x,'e: ',e)
            if x==0:
                print(xsub)
    return ''
findSub(ls:=[3, 4, -7, 3, 1, 3, 1, -4, -2, -2])