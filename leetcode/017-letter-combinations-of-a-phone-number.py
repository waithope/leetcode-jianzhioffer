#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(digits, table, index, path, res):
            if len(path) == len(digits):
                res.append(path)

            for i in range(index, len(digits)):
                for j in table[digits[i]]:
                    dfs(digits, table, i+1, path+j, res)

        if not isinstance(digits, str) or len(digits) == 0:
            return []
        table = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                 '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        dfs(digits, table, 0, '', res)
        return res

