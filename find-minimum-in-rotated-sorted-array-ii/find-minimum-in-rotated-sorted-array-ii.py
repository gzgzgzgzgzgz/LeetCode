class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            mid_value = nums[mid]
            #变化点在右边
            if mid_value > nums[r]:
                l = mid + 1
            elif mid_value < nums[r]:
                r = mid
            else:
                r-=1
        return nums[r]
                