class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        changed_node = 0
        l,r = 0, len(nums) - 1
        if nums[r] > nums[l]: return nums[l]
        while l < r:
            mid = (l+r) // 2
            mid_value = nums[mid]
            if mid_value > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
#         while l <= r:
#             mid = (l+r) // 2
#             mid_value = nums[mid]
#             if mid_value > nums[mid + 1]:
#                 changed_node = mid
#                 break
#             if mid_value < nums[mid - 1]:
#                 changed_node = mid
#                 break
#             if mid_value > nums[0]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         if nums[changed_node] < nums[changed_node - 1]:
#             return nums[changed_node]
#         else:
#             return nums[changed_node + 1]
                
            
            
            