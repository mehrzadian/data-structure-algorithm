class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
### making binary search tree ###
root = Node(15)
root.left = Node(10)
root.left.right = Node(12)
root.left.right.left = Node(11)
root.left.right.right = Node(13)
root.right = Node(25)
root.right.left = Node(20)
root.right.right = Node(40)
root.right.right.left = Node(30)
root.right.right.left.right = Node(35)
#
# #     15
# #    /  \
# #  10     25
# #   \   /  \
# #   12 20   40
# #  / \     /
# # 11 13   30
# #         \
# #         35
def inorderTraversal(root,ls):
    '''inorder traversal of binary tree'''
    if root:
        inorderTraversal(root.left,ls)
        ls.append(root)
        print(root.data, end=" ")
        inorderTraversal(root.right,ls)
    return ls
ls = inorderTraversal(root,[])
print()
def delete_right_side_of_root(root,ls):
    '''delete right side node of root
    and replace it with inorder successor'''
    #گره بعدی این گره را پیدا میکنیم در پیمایش inorder
    #و مقدار این گره برابر اون قرار میدیم
    #و آن گره را حذف میکنیم
    deleting = root.right
    for i in range(len(ls)):
        if ls[i] == deleting:
            deleting.data = ls[i+1].data
            ls[i+1] = ls[i+1].right
            ls.pop(i+1)
            break
    return ls
ls = delete_right_side_of_root(root,ls)

print()
for item in ls:
    print(item.data, end=" ")
print()
#     15
#    /  \
#  10     30
#   \   /  \
#   12 20   40
#  / \     /
# 11 13   35
def draw_tree(root):
    '''draw tree'''
    if root:
        print(root.data)
        if root.left:
            print("left of ",root.data," is ",root.left.data)
        if root.right:
            print("right of ",root.data," is ",root.right.data)
        draw_tree(root.left)
        draw_tree(root.right)

draw_tree(root)
