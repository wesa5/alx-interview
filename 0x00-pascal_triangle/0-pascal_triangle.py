#!/usr/bin/python3
'''Module to return pascal triangle'''

def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle
    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """

     
    if type(n) is not int:
        raise TypeError("n must be an integer")

    triangle = []

    if n <= 0:
        return triangle
    previous = [1]
    for index in range(n):
        rowlist = []
        if index == 0:
            rowlist = [1]
        else:
            for i in range(index + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == (index):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])
        previous = rowlist
        triangle.append(rowlist)
    return triangle
