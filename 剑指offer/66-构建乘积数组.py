# -*- coding:utf-8 -*-
'''
        构建乘积数组
=============================
给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其中B中的元素
B[i]=A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
'''

def buildProductionArray(array):
    '''
    思路：蛮力法就是每构建B中的一个元素，就遍历一遍A数组计算出乘积。但这种方法
    的时间复杂度为O(n)。一个更好的方法是只需遍历两边A数组就可以计算出B数组，B[i]
    的值可以看成两部分的乘积，即B[i]=A[0]x...A[i-1] * A[i+1]x...A[n-1]，而
    第一部分可以通过从头遍历A数组计算乘积获得，第二部分可以通过从尾遍历A数组计算乘积
    获得。第一次遍历时，B数组中的乘积值为第一部分的值，第二次遍历时在第一次遍历之后
    的B数组的基础上再乘上第二部分的值，最终就得到完整的B数组。
    '''
    if not isinstance(array, list) or len(array) == 0:
        return None

    result = [1]
    for i in range(1, len(array)):
        result.append(result[i - 1] * array[i - 1])

    temp = 1
    for i in range(len(array) - 2, -1, -1):
        temp *= array[i + 1]
        result[i] *= temp
    return result


import unittest

class TestBuildProductionArray(unittest.TestCase):
    def test_build_production_array(self):
        self.assertEqual(buildProductionArray([1,2,3,4,5]), [120,60,40,30,24])
        self.assertEqual(buildProductionArray([1,2,0,4,5]), [0,0,40,0,0])
        self.assertEqual(buildProductionArray([1,2,0,4,0]), [0,0,0,0,0])
        self.assertEqual(buildProductionArray([1,-2,3,-4,5]), [120,-60,40,-30,24])
        self.assertEqual(buildProductionArray([1,-2]), [-2, 1])


if __name__ == '__main__':
    unittest.main()