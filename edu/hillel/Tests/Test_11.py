"""
test11
"""

import random

matrix =[]
line_count = 5
column_count = 8

def t_matrix(mat):
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

def print_matrix(mat):
    for i in range(len(mat)):
        for x in mat[i]:
            print(x,end="\t")
        print()


def create_matrix(mat,line_count,column_count):
    for i in range(line_count):
        line = []
        for x in range(column_count):
            item = random.randrange(10)
            line.append(item)
        mat.append(line)
    return mat


def some_kind_of_sorting(mat):
    for i in range(len(mat)):
        if i % 2:
            mat[i].sort()
        else:
            mat[i].sort(reverse=True)
    return mat
#Дошло наконец,зачем нужны транспонированные матрицы:в них строки становятся стоблцами,а столбцы-строками
#далее-просто отсортировать четные и нечётные строки и заново транспонировать
new_matrix=create_matrix(matrix,line_count,column_count)
print("original:")
print_matrix(new_matrix)
print("sorted:")
print_matrix(t_matrix(some_kind_of_sorting(t_matrix(new_matrix))))