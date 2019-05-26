# -*- coding:utf-8 -*-
'''
    数组中的逆序对
======================
在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。例如，在数组{7,5,6,4}中，一共
存在5个逆序对，分别是(7,6)、(7,5)、(7,4)、(6,4)和(5,4)。
'''

def inversePairs(nums):
    '''
    用暴力破解的方法就是从左向右扫描数组，每扫描到一个数字，就比较该数字与其
    后面数组的大小。如果后面的数字比它小就构成一个逆序对。该方法的时间复杂度
    为O(n^2)，还存在一种以空间换时间的O(nlogn)的方法。具体思路如下:
    利用归并排序的思想，先将数组分割成长度为1的子数组，并对相邻的子数组统计
    逆序对，接着对相邻的子数组进行排序、合并为长度为2的子数组。然后对长度为
    2的相邻子数组统计其逆序对，具体方法是将一个指针l指向左子数组的末尾，另
    一个指针r指向右子数组的末尾，由于子数组内部已经排好序了。当l指向的元素
    大于r指向的元素时，说明右子数组中的元素都小于l指向的元素，所有将逆序对
    总数加上其数组长度，同时把l向前移动一格，指向左子数组的上一个元素；当l
    指向的元素小于r指向的元素时，不能构成逆序对，将r向前移动一格。按照上述
    过程递归下去，直到整个数组排序完成，就可以得到最终的逆序对总数了。
    '''

    def inversePairsCore(aux, nums, start, end):
        if start == end:
            aux[start] = nums[start]
            return 0

        mid = (end - start) // 2
        leftCount = inversePairsCore(aux, nums, start, start + mid)
        rightCount = inversePairsCore(aux, nums, start + mid + 1, end)

        i, j = (start + mid), end
        k = end
        count = 0
        while i >= start and j >= (start + mid + 1):
            if nums[i] > nums[j]:
                aux[k] = nums[i]
                count += (j - start - mid)
                i -= 1
            else:
                aux[k] = nums[j]
                j -= 1
            k -= 1

        while i >= start:
            aux[k] = nums[i]
            k -= 1
            i -= 1
        while j >= (start + mid + 1):
            aux[k] = nums[j]
            k -= 1
            j -= 1

        for i in range(start, end+1):
            nums[i] = aux[i]

        return (leftCount + rightCount + count)

    if not isinstance(nums, list) or len(nums) == 0:
        return 0
    aux = [0] * len(nums)
    res = inversePairsCore(aux, nums, 0, len(nums) - 1)
    return res

import unittest

class TestInversePairs(unittest.TestCase):
    def test_inverse_pairs(self):
        self.assertEqual(inversePairs(None), 0)
        self.assertEqual(inversePairs([1]), 0)
        self.assertEqual(inversePairs([1,2]), 0)
        self.assertEqual(inversePairs([2,1]), 1)
        self.assertEqual(inversePairs([1,2,3,4,5,6]), 0)
        self.assertEqual(inversePairs([6,5,4,3,2,1]), 15)
        self.assertEqual(inversePairs([1,2,3,4,7,6,5]), 3)
        self.assertEqual(inversePairs([1,2,1,2,1]), 3)


if __name__ == '__main__':
    unittest.main()