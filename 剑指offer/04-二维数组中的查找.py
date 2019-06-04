# -*- coding:utf-8 -*-
'''
    二维数组中的查找
======================
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下
递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组
中是否含有整数。如果找到该整数，则返回True；否则，返回False。
1  2  8  9
2  4  9  12
4  7  10 13
6  8  11 15
在以上数组中查找数字7，则返回True；查找数字5，返回False。
'''

def find(matrix, number):
    '''
    时间O(n)，空间O(1)
    '''
    if len(matrix) <= 0:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    i, j = 0, cols - 1
    while i < rows and j > 0:
        if matrix[i][j] == number:
            return True
        elif matrix[i][j] > number:
            j -= 1
        else:
            i += 1
    return False


import unittest

class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(find([[1, 2, 8, 9],
                               [2, 4, 9, 12],
                               [4, 7, 10, 13],
                               [6, 8, 11, 15]], 3), False)

if __name__ == '__main__':
    unittest.main()