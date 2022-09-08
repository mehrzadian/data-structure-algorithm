# Given an array containing only 0’s, 1’s, and 2’s, sort it in linear time and using constant space.
def sort(ls):
    ones=0
    zeros=0
    twos=0
    for x in ls:
        if x==0:
            zeros+=1
        elif x==1:
            ones+=1
        else:
            twos+=1
    return [0]*zeros+[1]*ones+[2]*twos
print(sort([1,1,1,0,0,1,0]))
