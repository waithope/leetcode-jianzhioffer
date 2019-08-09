'''
小多想在美化一下自己的庄园。他的庄园毗邻一条小河，他希望在河边种一排树，共 M 棵。小多采购了 N 个品种的树，每个品种的数量是 Ai (树的总数量恰好为 M)。但是他希望任意两棵相邻的树不是同一品种的。小多请你帮忙设计一种满足要求的种树方案。
输入描述：
第一行包含一个正整数 N，表示树的品种数量。
第二行包含 N 个正整数，第 i (1 <= i <= N) 个数表示第 i 个品种的树的数量。
数据范围：
1 <= N <= 1000
1 <= M <= 2000

输出描述：
输出一行，包含 M 个正整数，分别表示第 i 棵树的品种编号 (品种编号从1到 N)。若存在多种可行方案，则输出字典序最小的方案。若不存在满足条件的方案，则输出"-"。

输入例子：
3
4 2 1

输出例子：
1 2 1 2 1 3 1
'''

def indexOfMax(array):
    maxNum, index = 0, -1
    for i in range(len(array)):
        if array[i] > maxNum:
            index = i
            maxNum = array[i]
    return index

def dfs(nums, res, n, m, step):
    max_i = indexOfMax(nums)
    if max_i == -1:
        return True
    if nums[max_i] * 2 > m + 1:
        return False
    if nums[max_i] * 2 == m + 1:
        nums[max_i] -= 1
        m -= 1
        res[step] = max_i + 1
        if dfs(nums, res, n, m, step + 1):
            return True
        nums[max_i] += 1
        m += 1
    else:
        for i in range(n):
            if nums[i] > 0 and (res[step - 1] != i + 1 or step == 0):
                nums[i] -= 1
                m -= 1
                res[step] = i + 1
                if dfs(nums, res, n, m, step + 1):
                    return True
                nums[i] += 1
                m += 1
    return False

if __name__ == '__main__':
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    m = sum(nums)
    res = [0] * m
    if dfs(nums, res, n, m, 0):
        print(' '.join(map(str, res)))
    else:
        print('-')