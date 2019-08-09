'''
给定一个长度为偶数的数组arr，将该数组中的数字两两配对并求和，在这些和中选出最大和最小值，请问该如何两两配对，才能让最大值和最小值的差值最小？

输入描述：
一共2行输入。
第一行为一个整数n，2<=n<=10000, 第二行为n个数，组成目标数组，每个数大于等于2，小于等于100。

输出描述：
输出最小的差值。

输入例子：
4
2 6 4 3

输出例子：
1
'''

if __name__ == '__main__':
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    nums = sorted(nums)
    minNum, maxNum = 2 ** 32, -(2 ** 32)
    left, right = 0, len(nums) - 1
    while left < right:
        temp = nums[left] + nums[right]
        if temp < minNum:
            minNum = temp
        if temp > maxNum:
            maxNum = temp
        left += 1
        right -= 1
    print(maxNum - minNum)
