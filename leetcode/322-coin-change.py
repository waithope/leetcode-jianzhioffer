#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (not isinstance(coins, list) or len(coins) <= 0
            or not isinstance(amount, int) or amount < 0):
            return -1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]

