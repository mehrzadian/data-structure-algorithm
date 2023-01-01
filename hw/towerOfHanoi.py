import turtle
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
