class Node:
    def __init__(self, data):
        '''In threaded tree, nodes need two more fields which can be 0 or 1 '''
        self.data = data
        self.left = None
        self.right = None
        self.lthread = 0
        self.rthread = 0


############ 3 this function does'nt work properly  ################
def makeBinTree(preorderTree='ABCDEFGHI', inorderTree='BCAEDGHFI'):
    '''as expalined in page 74 of unit 5 slides,
    find tree and make it from pre-in oreder of it'''
    root = Node(preorderTree[0])
    rootIndex = inorderTree.find(preorderTree[0])

    if (len(inorderTree[0:rootIndex]) and len(inorderTree[rootIndex+1:])) == 0:
        return root

    root.left = makeBinTree(
        preorderTree[1:1+rootIndex], inorderTree[0:rootIndex])
    root.right = makeBinTree(
        preorderTree[1+rootIndex:], inorderTree[rootIndex+1:])
    return root

######## قسمت اول سوال پروژه شامل این تابع هست ######
def preorderTraversal(root, ls):
    '''make a list from preorder traversal of tree'''
    if root:
        ls.append(root)
        print(root.lthread, "  ", root.data, "  ", root.lthread)
        #اگر سمتی از آن به صورت نخ وصل شده باشد نباید در تابع بازگشتی بیاید 
        #چون باعث میشه تو حلقه بینهایت بیفتیم
        if root.lthread == 0:
            preorderTraversal(root.left, ls)
        if root.rthread == 0:
            preorderTraversal(root.right, ls)
    return ls




root = Node(5)
root.left = Node(11)
root.left.left = Node(17)
root.right = Node(6)
root.right.left = Node(15)
root.right.right = Node(8)
root.right.right.left = Node(23)
root.right.right.right = Node(45)
print("before making thread: ")
ls = preorderTraversal(root, [])
print()
print()
print()

######## قسمت اول سوال پروژه شامل این تابع هست ######
def threadedBinTree(ls):
    # تمام گره ها بررسی میشن 
    #اگر گره راستی خالی بود، به عنصر بعدی لیست اشاره خواهد کرد
    # اگر چپش خالی بود به عنصر قبلی
    for i, item in enumerate(ls):
        if item.left is None:
            item.lthread = 1
            item.left = ls[i-1]
            print("left thread of ",item.data," is ",item.left.data)
        if item.right is None:
            item.rthread = 1
            item.right = ls[i-1]
            print("right thread of ",item.data," is ",item.right.data)


threadedBinTree(ls)
print("After making thread: ")
ls = preorderTraversal(root, [])
# تست
#     5
#    /  \
#  11     6
#   /   /  \
# 17   15    8
#           / \
#         23   45

######## قسمت دوم سوال پروژه شامل این تابع هست ######
def inorderTraversal(root,ls):
    if root:
        if root.lthread == 0:
            inorderTraversal(root.left,ls)
        ls.append(root)
        print(root.data, end=" ")
        if root.rthread == 0:
            inorderTraversal(root.right,ls)
    return ls

inorderTraversal(root,[])
print()
#ورودی های مختلف تست شده، خودتونم میتونید بهش ورودی بدید
after_the_node = int(input("in the right side of which node do you want to insert? "))
data = int(input("please enter the data of new node: "))
node =Node(data)
######## قسمت دوم سوال پروژه شامل این تابع هست ######
def insert(ls,after_the_node,node):
    #به ازای هر گره ای میریم جلو 
    #هر وقت به گره درخواستی رسیدیم متوقف میشیم
    #و چک میکنیم آیا سمت راستش خالی هست یا نه 
    # اگر بود که گره جدید و اضافه 
    #وگرنه قسمت راست گره را نگه میداریم و به قسمت راست گره جدید میریزیم
     
    for item in ls:
        if item.data == after_the_node:
            if item.right is None:
                item.right = node
            else:
                temp = item.right
                item.right = node
                node.right = temp
#برای تست از درختی که در بخش قبل پروژه بود استفاده شده

insert(ls,after_the_node,node)
inorderTraversal(root,[])
#another traversing for check
print()
preorderTraversal(root,[])