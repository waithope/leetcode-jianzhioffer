# -*- coding:utf-8 -*-
'''
    礼物的最大价值
=======================
在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格直到到达
棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
'''

def getMaxValue1(matrix):
    '''
    思路：这题是一个动态规划题，假设函数f(i,j)表示到达坐标(i,j)时能拿到
    礼物的最大值，因此f(i,j) = max(f(i-1, j), f(i, j-1)) + gift(i, j)
    当到达右下角终点是也就获得了全局的礼物最大值。

    时间效率O(n^2)，空间效率O(n^2)
    '''
    if (not isinstance(matrix, list) or len(matrix) == 0
        or not isinstance(matrix[0], list) or len(matrix[0]) == 0):
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    maxValue = [[0]*cols for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            up, left = 0, 0
            if i > 0:
                up = maxValue[i-1][j]
            if j > 0:
                left = maxValue[i][j-1]
            maxValue[i][j] = max(up, left) + matrix[i][j]
    return maxValue[-1][-1]


def getMaxValue2(matrix):
    '''
    可以将第一个方法中额外建立的二维数组优化为一维数组
    时间效率O(n^2)，空间效率O(n)
    '''
    if (not isinstance(matrix, list) or len(matrix) == 0
        or not isinstance(matrix[0], list) or len(matrix[0]) == 0):
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    maxValue = [0] * cols

    for i in range(rows):
        for j in range(cols):
            up, left = 0, 0
            if i > 0:
                up = maxValue[j]
            if j > 0:
                left = maxValue[j-1]
            maxValue[j] = max(up, left) + matrix[i][j]
    return maxValue[-1]

import unittest

class TestGetMaxValue(unittest.TestCase):
    def test_get_max_value1(self):
        self.assertEqual(getMaxValue1([[1,2,3],[4,5,6],[7,8,9]]), 29)
        self.assertEqual(getMaxValue1([[1,10,3,8],
                                       [12,2,9,6],
                                       [5,7,4,11],
                                       [3,7,16,5]]), 53)
        self.assertEqual(getMaxValue1([[1,10,3,8]]), 22)
        self.assertEqual(getMaxValue1([[1],[12],[5],[3]]), 21)
        self.assertEqual(getMaxValue1([[3]]), 3)
        self.assertEqual(getMaxValue1(None), 0)
        self.assertEqual(getMaxValue2([[1,2,3],[4,5,6],[7,8,9]]), 29)
        self.assertEqual(getMaxValue2([[1,10,3,8],
                                       [12,2,9,6],
                                       [5,7,4,11],
                                       [3,7,16,5]]), 53)
        self.assertEqual(getMaxValue2([[1,10,3,8]]), 22)
        self.assertEqual(getMaxValue2([[1],[12],[5],[3]]), 21)
        self.assertEqual(getMaxValue2([[3]]), 3)
        self.assertEqual(getMaxValue2(None), 0)



if __name__ == '__main__':
    unittest.main()