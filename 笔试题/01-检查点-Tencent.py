'''
    检查点
===============
在一场比赛中有n个检查点，比赛要求是到达n-1个检查点即可。这些检查点排列在
x轴上，位置分别为x1,x2,x3...xn，且允许以任意顺序访问检查点。比赛的开始
位置为a，则完成比赛所需经过的最小距离。
其中:
1 <= n <= 100000,
-1000000 <= a <= 1000000,
-10000000 <= xi <= 1000000

Example1:
输入：n = 3, start = 10, nums=[1, 7, 12]
输出：7
'''


def checkNPoint(n, start, nums):
    '''
    提示：主要分三种情况，
    1. 当起始位置在x1上或者在其左侧以及在xn上或者在其右侧，只需分别计算一次路线
    2. 当起始位置在x2上或者x1，x2之间以及在xn-1上或者xn-1,xn之间，需分别计算三种路线
    3. 当起始位置不是以上的情况下，在x2和xn-1之间，需分别计算四种路线
    '''
    if not isinstance(n, int) or n < 1 or n > 100000:
        return
    if not isinstance(start, int) or start < -1000000 or n > 1000000:
        return
    if not isinstance(nums, list) or len(nums) <= 0 or len(nums) != n:
        return

    if start <= nums[0]:
        return nums[n-2] - start
    elif start >= nums[-1]:
        return start - nums[1]
    elif start > nums[0] and start <= nums[1]:
        candidate1 = nums[-1] - start
        candidate2 = 2 * (nums[-2] - start) + (start - nums[0])
        candidate3 = nums[-2] - start + 2 *(start - nums[0])
        return min(candidate1, candidate2, candidate3)
    elif start >= nums[-2] and start < nums[-1]:
        candidate1 = start - nums[0]
        candidate2 = 2 * (start - nums[1]) + (nums[-1] - start)
        candidate3 = (start - nums[1]) + 2 * (nums[-1] - start)
        return min(candidate1, candidate2, candidate3)
    else:
        candidate1 = 2 * (start - nums[1]) + (nums[-1] - start)
        candidate2 = 2 * (start - nums[0]) + (nums[-2] - start)
        candidate3 = 2 * (nums[-1] - start) + (start - nums[1])
        candidate4 = 2 * (nums[-2] - start) + (start - nums[0])
        return min(candidate1, candidate2, candidate3, candidate4)



import unittest

class TestCheckNPoint(unittest.TestCase):
    def test_check_n_point(self):
        self.assertEqual(checkNPoint(3, 10, [1, 7, 12]), 7)
        self.assertEqual(checkNPoint(5, 1, [1, 3, 5, 20, 21]), 19)
        self.assertEqual(checkNPoint(5, 21, [1, 3, 5, 20, 21]), 18)
        self.assertEqual(checkNPoint(5, 10, [1, 3, 5, 20, 21]), 25)


if __name__ == '__main__':
    unittest.main()