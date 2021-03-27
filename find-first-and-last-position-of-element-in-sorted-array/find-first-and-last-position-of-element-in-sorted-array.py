class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def binarysearchleft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] >= target:
                    right = mid -1
                else:
                    left = mid + 1
            return left
        i, j = 0, len(nums) - 1
        left = binarysearchleft(nums, target)
        right = binarysearchleft(nums, target + 1)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        return [left, right-1]
