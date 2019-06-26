#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        思路：1~n的所有n个点，每个点都可以作为根节点，根据点选取的位置可以
        分两种情况。假设n=3，选择点2为根节点后，左子树中的内容只能是点2左边
        的数，右子树中的内容只能是点2右边的数。显然，这是一个递归的过程。设
        原问题为G(n)，表示n个点时能组成的BST的数目。所有G(n)的结果为根节点
        分别取1,2,...n时的BST数目总和。因此，G(n) = G(0)*G(n-1)+G(1)*
        G(n-2)+...+G(n-1)*G(0)，其中G(0)=G(1)=1
        '''
        if not isinstance(n ,int) or n < 1:
            return 0

        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]


