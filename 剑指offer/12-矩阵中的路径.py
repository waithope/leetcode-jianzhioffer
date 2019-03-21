# -*- coding:utf-8 -*-
'''
    矩阵中的路径
==================
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面
3x4的矩阵中包含一条字符串"bfce"的路径。但矩阵中不包含字符串"abfb"的路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入
这个格子。
[
    [a, b, t, g],
    [c, f, c, s],
    [j, d, e, h]
]
'''

def hasPath(matrix, word):
    '''
    回溯法：路径可以看成一个栈，当在矩阵中定位了路径中前k个字符的位置之后，
    在与第k个字符对应的格子的周围都没有找到第k+1个字符，这时候就回到第k-1个
    字符，重新定位第k个字符。
    注：由于路径不能重复进入矩阵的格子，需要标识路径是否已经进入每一个格子。
    '''
    if not isinstance(matrix, list) or len(matrix) <= 0:
        return False
    if not isinstance(word, str) or len(word) <= 0:
        return False

    def exist(matrix, row, col, start):
        if start >= len(word):
            return True
        if (row < 0 or row >= len(matrix)
            or col < 0 or col >= len(matrix[0])):
            return False

        if matrix[row][col] == word[start]:
            start += 1
            ch = matrix[row][col]
            matrix[row][col] = False

            hasPath = (exist(matrix, row, col-1, start)
                        or exist(matrix, row-1, col, start)
                        or exist(matrix, row, col+1, start)
                        or exist(matrix, row+1, col, start))

            matrix[row][col] = ch
            return hasPath
        return False

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if exist(matrix, row, col, 0):
                return True
    return False


import unittest

class TestHasPath(unittest.TestCase):
    def test_has_path(self):
        self.assertEqual(hasPath([['a','a','a','a']], 'ab'), False)
        self.assertEqual(hasPath([['a','a','a','a']], 'aaaa'), True)
        self.assertEqual(hasPath([['b'],['a'],['a'],['a']], 'baa'), True)
        self.assertEqual(hasPath([['a','b','t','g'],['c','f','c','s'],['j','d','e','h']],
                                    'bfce'), True)


if __name__ == '__main__':
    unittest.main()

