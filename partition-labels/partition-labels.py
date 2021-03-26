class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = dict()
        res = []
        #record the farthest location of each letter
        for i in range(len(S)):
            dic[S[i]] = i
        curFarthest = 0
        curStart = 0
        for j in range(len(S)):
            if dic[S[j]] > curFarthest:
                curFarthest = dic[S[j]]
            if j == curFarthest:
                res.append(curFarthest - curStart + 1)
                curStart = curFarthest + 1
        return res
            