class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key = lambda a: a[1])
        res = 1
        curEnd = points[0][1]
        for i in points:
            if i[0] <= curEnd and curEnd <= i[1]:
                continue
            else:
                curEnd = i[1]
                res += 1
        return res