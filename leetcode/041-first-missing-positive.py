#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if not isinstance(nums, list):
        #     return

        # if len(nums) <= 1:
        #     return 1

        # nums.append(0)
        # nums = sorted(nums)
        # res = 0
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] > 1:
        #         res = nums[i - 1] + 1
        #         if res <= 0:
        #             continue
        #         return res
        # if nums[-1] == 0:
        #     return 1
        # else: return nums[-1] + 1

        for i in range(len(nums)):
            while (nums[i] > 0 and nums[i] < len(nums)
                and nums[nums[i] - 1] != nums[i]):
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


