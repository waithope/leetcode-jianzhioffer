# -*- coding:utf-8 -*-
'''
    最小的k个数
==================
输入n个整数，找出其中最小的k个数。例如，输入4、5、1、6、2、7、3、8这8个数，
则最小的4个数字是1、2、3、4。
'''

import random
def partition(nums, start, end):
    if (not isinstance(nums, list) or len(nums) <= 0
        or start < 0
        or end > len(nums)):
        raise ValueError('Invalid Parameter')

    index = random.randint(start, end)
    nums[index], nums[end] = nums[end], nums[index]
    small = start - 1
    for i in range(start, end):
        if nums[i] < nums[end]:
            small += 1
            if small != i:
                nums[i], nums[small] = nums[small], nums[i]

    small += 1
    nums[small], nums[end] = nums[end], nums[small]
    return small

def numberOfKLeastNum1(nums, k):
    '''
    解法一：利用快排的partition函数进行随机选择，只对包含最小的K个数范围进行快排，
    期望运行时间为O(n)，同时会修改原数组。
    证明在算法导论第9章第2节期望为线性时间的选择算法。
    '''
    if (not isinstance(nums, list) or len(nums) <= 0
        or not isinstance(k, int)
        or k > len(nums) or k <= 0):
        return
    start, end = 0, len(nums) - 1
    index = partition(nums, start, end)
    while index != (k - 1):
        if index > k - 1:
            end = index - 1
            index = partition(nums, start, end)
        else:
            start = index + 1
            index = partition(nums, start, end)

    return sorted(nums[:k])


import heapq
def numberOfKLeastNum2(nums, k):
    '''
    解法二：维护一个大小为k的最大堆，先将数组的前k个元素直接读入到堆中，并
    进行堆化，然后从第k个位置（下标从0开始）依次读取数组元素，并与最大堆的
    堆顶元素（堆中最大值）比较，如果小于堆顶元素，则弹出堆顶元素，插入当前
    元素，否则，跳过，读取数组中下一个元素。
    时间复杂度O(nlgk)，不会修改原数组，适合海量数据的处理。
    '''
    if (not isinstance(nums, list) or len(nums) <= 0
        or not isinstance(k, int) or k > len(nums)
        or k <= 0):
        return None

    maxHeap = []
    for i, num in enumerate(nums):
        if i < k:
            heapq.heappush(maxHeap, -1 * num)
        else:
            heapq.heappushpop(maxHeap, -1 * num)

    return sorted(list(map(lambda x: -x, maxHeap)))


import unittest
class TestNumberOfKLeastNum(unittest.TestCase):
    def test_number_of_k_least_num(self):
        self.assertEqual(numberOfKLeastNum1([4,5,1,6,2,7,3,8], 4),
                         [1,2,3,4])
        self.assertEqual(numberOfKLeastNum1([4,5,1,6,2,7,3,8], 8),
                         [1,2,3,4,5,6,7,8])
        self.assertEqual(numberOfKLeastNum1([4,5,1,6,2,7,3,8], 10),
                         None)
        self.assertEqual(numberOfKLeastNum1([4,5,1,6,2,7,3,8], 1),
                         [1])
        self.assertEqual(numberOfKLeastNum1([4,5,1,6,2,7,3,8], 0),
                         None)
        self.assertEqual(numberOfKLeastNum2([4,5,1,6,2,7,3,8], 4),
                         [1,2,3,4])
        self.assertEqual(numberOfKLeastNum2([4,5,1,6,2,7,3,8], 8),
                         [1,2,3,4,5,6,7,8])
        self.assertEqual(numberOfKLeastNum2([4,5,1,6,2,7,3,8], 10),
                         None)
        self.assertEqual(numberOfKLeastNum2([4,5,1,6,2,7,3,8], 1),
                         [1])
        self.assertEqual(numberOfKLeastNum2([4,5,1,6,2,7,3,8], 0),
                         None)


if __name__ == '__main__':
    unittest.main()