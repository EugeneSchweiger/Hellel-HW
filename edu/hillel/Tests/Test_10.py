"""
test10 Transported matrix
"""
import pprint
matrix = [[1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4]]

# pprint.pprint(matrix)

def t_matrix(mat):
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
# pprint.pprint(t_matrix(matrix),width=30)



def print_matrix(mat):
    for i in range(len(mat)):
        for x in mat[i]:
            print(x,end="\t")
        print()
print_matrix(matrix)
print_matrix(t_matrix(matrix))
