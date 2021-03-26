import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        res = -math.inf
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
            res=max(res, dp[i])
        return max(dp[0], res)
