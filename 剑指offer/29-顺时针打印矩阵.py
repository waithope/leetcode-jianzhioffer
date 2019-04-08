# -*- coding:utf-8 -*-
'''
    顺时针打印矩阵
====================
输入一个矩阵，按照从外向里以顺时针依次打印出每一个数字。例如，如果输入以下矩阵：
[
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
'''

def printMatrix(matrix):
    if not isinstance(matrix, list) or len(matrix) <= 0:
        return

    res = []
    rowStart, rowEnd = 0, len(matrix) - 1
    colStart, colEnd = 0, len(matrix[0]) - 1
    while (rowStart <= rowEnd) and (colStart <= colEnd):
        for i in range(colStart, colEnd + 1):
            res.append(matrix[rowStart][i])
        rowStart += 1

        for i in range(rowStart, rowEnd + 1):
            res.append(matrix[i][colEnd])
        colEnd -= 1

        for i in range(colEnd, colStart - 1, -1):
            res.append(matrix[rowEnd][i])
        rowEnd -= 1

        for i in range(rowEnd, rowStart - 1, -1):
            res.append(matrix[i][colStart])
        colStart += 1
    return res


import unittest

class TestPrintMatrix(unittest.TestCase):
    def test_print_matrix(self):
        self.assertEqual(printMatrix([[1]]), [1])
        self.assertEqual(printMatrix([[1,2],
                                      [3,4]]), [1,2,4,3])
        self.assertEqual(printMatrix([[1,2,3,4],
                                      [5,6,7,8],
                                      [9,10,11,12],
                                      [13,14,15,16]]),
                                      [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])
        self.assertEqual(printMatrix([[1,2],
                                      [3,4],
                                      [5,6],
                                      [7,8],
                                      [9,10]]),
                                      [1,2,4,6,8,10,9,7,5,3])

if __name__ == '__main__':
    unittest.main()