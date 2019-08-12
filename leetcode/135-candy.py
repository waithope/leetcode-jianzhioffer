#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not isinstance(ratings, list) or len(ratings) == 0:
            return 0

        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 1, 0, -1):
            if (ratings[i - 1] > ratings[i]
                and candies[i - 1] <= candies[i]):
                candies[i - 1] = candies[i] + 1

        return sum(candies)

