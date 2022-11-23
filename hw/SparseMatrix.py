rows, columns = int(input()), int(input())
ls = list()
for i in range(rows):
    innerLs = list()
    for j in range(columns):
        innerLs.append(int(input()))
    ls.append(innerLs)
print(ls)
size = 0
matrix = list()
for row in range(rows):
    for column in range(columns):
        if ls[row][column] != 0:
            size += 1
            matrix.append([row, column, ls[row][column]])
matrix.append([rows, columns, size])
print(matrix)
#example
# 5
# 6
# 0
# 0
# 0
# 0
# 9
# 0
# 0
# 8
# 0
# 0
# 0
# 0
# 4
# 0
# 0
# 2
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 5
# 0
# 0
# 2
# 0
# 0
# 0