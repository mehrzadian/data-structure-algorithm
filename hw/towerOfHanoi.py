import math
import stack 
n = int(input())


def moveDisk(disk, fromPole, toPole,):
    print("moving disk", disk, "from", fromPole, "to", toPole)
def hanoi(n,fromPole,toPole,withHelp):
    if n==1:
        moveDisk(n,fromPole,toPole)
    else:
        hanoi(n-1,fromPole,withHelp,toPole)
        moveDisk(n,fromPole,toPole)
        hanoi(n-1,withHelp,toPole,fromPole)
hanoi(n,1,3,2)
def hanoiI(n,fromPole,toPole,withHelp):
    '''Iterative version of the hanoi function
    input: n is the number of disks, fromPole is the pole where the disks are at the beginning,
     toPole is the pole where the disks are at the end,
      withHelp is the pole that is used to help move the disks'''
    numberOfMoves = int(math.pow(2,n)) -1
    S =stack.stack(n)
    D = stack.stack(n)
    A = stack.stack(n)
    
    
    for i in range(n,0,-1):
        S.push(i)
    print(S,D,A)
    
    for i in range(numberOfMoves):
        if i%3==0:
            if S.peek()<D.peek():
                D.push(S.pop())
            else:
                S.push(D.pop())
        elif i%3==1:
            if S.peek()<A.peek():
                A.push(S.pop())
            else:
                
                S.push(A.pop())
        else:
            if A.peek()>D.peek():
                A.push(D.pop())
            else:
                
                D.push(A.pop())
    if n%2==0:
        return A
    return D
print(hanoiI(n,1,3,2))




           