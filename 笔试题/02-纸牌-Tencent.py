'''
    纸牌
============
有一叠纸牌，一共有n张，从上往下依次编号为1到n，现在对这堆纸牌重复以下操作：
把当前位于顶端的牌扔掉，然后把新的顶端的牌放到整叠牌的底部。
最终一直操作到只剩下一张纸牌为止，最终输出每次丢掉的纸牌的编号。
输入：n, 1<=n<=1000000
输出：每次丢掉的纸牌的编号
'''


from collections import deque
def getCardsNum(n):
    '''
    利用python自带的队列deque实现题目要求，也可以通过公式，但实现起来比较麻烦
    时间O(n), 空间O(n)
    '''
    if not isinstance(n, int) or n < 1 or n > 1000000:
        return
    if n == 1:
        return [n]
    nums = deque([i for i in range(1, n+1)])
    res = []
    while len(nums) > 1:
        res.append(nums.popleft())
        num = nums.popleft()
        nums.append(num)
    res.append(nums[0])
    return res


import unittest

class TestGetCardsNum(unittest.TestCase):
    def test_get_cards_num(self):
        self.assertEqual(getCardsNum(1), [1])
        self.assertEqual(getCardsNum(2), [1, 2])
        self.assertEqual(getCardsNum(3), [1, 3, 2])
        self.assertEqual(getCardsNum(7), [1, 3, 5, 7, 4, 2, 6])


if __name__ == '__main__':
    unittest.main()