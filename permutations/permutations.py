class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = []
        def backtacking(nums,track):
            if len(nums) == len(track):
                ans.append(track[:])
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                backtacking(nums, track)
                track.pop()
        backtacking(nums, l)
        return ans

# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
    
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择