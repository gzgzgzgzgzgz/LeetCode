class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 用单调递减队列和deque解决
        if not nums or not k: return 0
        deque = collections.deque()
        # initialize deque
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)):
            #看看需不需要移除deque的首元素 因为deque里需要为当前窗口的元素
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res
        