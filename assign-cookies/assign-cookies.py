class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s: return 0
        s.sort()
        g.sort()
        index_s = len(s) - 1
        result = 0
        for i in range(len(g)-1,-1,-1):
            if s[index_s] >= g[i] and index_s >= 0:
                result+=1
                index_s-=1
        return result