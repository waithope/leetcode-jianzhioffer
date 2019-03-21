# -*- coding:utf-8 -*-
'''
    机器人的运动范围
======================
地上有一个m行n列的方格。一个机器人从坐标(0,0)的格子开始移动，它每次可以向左、
右、上、下移动一格，但不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k
为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。但它不能进入方格(35, 38),
因为3+5+3+8=19。请问机器人能够达到多少格子？
'''

def movingCount(threshold, rows, cols):
    '''
    '''
    def sumDigit(x):
        sum_ = 0
        while x > 0:
            sum_ += x % 10
            x //= 10
        return sum_

    def movingCount(threshold, row, col, visited):
        if (row < 0 or row >= len(visited)
            or col < 0 or col >= len(visited[0])):
            return 0
        if ((sumDigit(row) + sumDigit(col)) > threshold
            or visited[row][col] == True):
            return 0

        count = 0
        visited[row][col] = True
        count = (1 + movingCount(threshold, row, col-1, visited)
                   + movingCount(threshold, row-1, col, visited)
                   + movingCount(threshold, row, col+1, visited)
                   + movingCount(threshold, row+1, col, visited))
        return count

    if (not isinstance(threshold, int)
        or not isinstance(rows, int)
        or not isinstance(cols, int)
        or threshold < 0
        or rows <= 0
        or cols <= 0):
        return 0

    visited = [[False for j in range(cols)] for i in range(rows)]

    count = movingCount(threshold, 0, 0, visited)

    return count



import unittest

class TestMovingCount(unittest.TestCase):
    def test_moving_count(self):
        self.assertEqual(movingCount(5,10,10), 21)
        self.assertEqual(movingCount(15,20,20), 359)
        self.assertEqual(movingCount(10,1,10), 10)
        self.assertEqual(movingCount(15,100,1), 79)
        self.assertEqual(movingCount(15,10,1), 10)
        self.assertEqual(movingCount(15,1,1), 1)
        self.assertEqual(movingCount(0,1,1), 1)
        self.assertEqual(movingCount(-10,10,10), 0)


if __name__ == '__main__':
    unittest.main()