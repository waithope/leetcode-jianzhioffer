#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#
import collections
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        dic = collections.Counter(ages)
        res = 0
        for ageA, cntA in dic.items():
            for ageB, cntB in dic.items():
                if 0.5 * ageA + 7 < ageB <= ageAnowcoder.com/discuss/216062?type=post&order=time&pos=&page=5:
                    res += ageA * ageB
                    if ageA == ageB:
                        res -= ageA
        return res

