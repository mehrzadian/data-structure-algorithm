def sort(ls):
    zeros=[]
    ones=[]
    for i in range(len(ls)):
        if ls[i] == 0:
            zeros.append(0)
        else:
            ones.append(1)
    return zeros+ones
print(sort([0,1,0,1,0,1,1,1,0,0,0]))