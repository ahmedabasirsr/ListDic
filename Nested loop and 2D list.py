# Nested loop and 2D list

#2dlist = [
#         col0 col1 col2
#row0     [1,   2,   3],
#row1     [4,   5,   6],
#row2     [7,   8,   8],
#row3     [0]


list_2d=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8],
    [0]
]
print("Print value in 2 row and 1 column: ",list_2d[2][1])
print("***********************************************")
for row in list_2d :
    print(row)
    print("*******")
    for col in row:
        print(col)

print("*******************************************************")


