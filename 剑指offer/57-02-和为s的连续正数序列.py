# -*- coding:utf-8 -*-
'''
    和为s的连续正数序列
============================
输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。例如输入15，
由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、4～6和7～8。
'''

def findContinuousSequence(target):
    '''
    思路：用两个数left, right来分别表示连续序列的最小值和最大值，如果从left
    到right的序列和大于s，则增大left的值；如果从left到right的序列和小于s，则
    增大right的值；直到一直增加left到target的中间数为止，表示后面的序列都是大于
    s的，没有有效的正数序列了。
    '''
    if not isinstance(target, int):
        return None

    left, right = 1, 2
    middle = (target + 1) // 2
    while left < middle:
        sequence = [num for num in range(left, right+1)]
        s = sum(sequence)
        if s == target:
            print(sequence)
            right += 1
        elif s > target:
            left += 1
        else:
            right += 1


if __name__ == '__main__':
    findContinuousSequence(1)
    findContinuousSequence(3)
    findContinuousSequence(4)
    findContinuousSequence(9)
    findContinuousSequence(15)
