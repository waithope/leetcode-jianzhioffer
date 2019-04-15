# -*- coding:utf-8 -*-
'''
    二叉搜索树的后序遍历序列
=============================
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回True，
否则返回False。假设输入的数组的任意两个数字都互不相同。例如，输入数组{5,7,6,9
11,10,8}，则返回True，因为这个整数序列是下图二叉搜索树的遍历结果。如果输入的
数组是{7,4,6,5}，则由于没有哪棵二叉搜索树的后序遍历结果是这个序列，因此返回False。
#         8
#     6      10
#   5   7  9    11
'''

def isPostOrder(nums):
    '''
    思路：在二叉搜索树后序遍历序列数组中，数组最后一个元素的值是根节点的值，
    其前面的数字可以分为两个部分，第一部分是左子树节点的值，都比根节点的值小；
    第二部分是右子树节点的值，都比根节点的值大。由于是树结构，这种形式是递归
    成立的。所以我们可以通过遍历根节点前面部分的数字，与根节点的值进行比较，
    找到左子树与右子树的分割点，接着递归的进行判断。
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return False

    root = nums[-1]
    for i, element in enumerate(nums):
        if element > root:
            break
    for j, element in enumerate(nums[i:-1]):
        if element < root:
            return False

    left = True
    if i > 0:
        left = isPostOrder(nums[:i])
    right = True
    if i < len(nums) - 1:
        right = isPostOrder(nums[i:-1])

    return left and right


import unittest

class TestIsPostOrder(unittest.TestCase):
    def test_is_post_order(self):
        self.assertEqual(isPostOrder([4,8,6,12,16,14,10]), True)
        self.assertEqual(isPostOrder([4,6,7,5]), True)
        self.assertEqual(isPostOrder([1,2,3,4,5]), True)
        self.assertEqual(isPostOrder([5,4,3,2,1]), True)
        self.assertEqual(isPostOrder([5]), True)
        self.assertEqual(isPostOrder([7,4,6,5]), False)
        self.assertEqual(isPostOrder([4,6,12,8,16,14,10]), False)
        self.assertEqual(isPostOrder(None), False)


if __name__ == '__main__':
    unittest.main()


