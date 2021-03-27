class Solution:
    #剑指offer 58
    def reverseWords(self, s: str) -> str:
        res = []
        s = s.strip()
        head, tail = len(s) -1 , len(s) - 1
        while head >= 0:
            while s[head] != " " and head >= 0:
                head-=1
            res.append(s[head+1:tail+1])
            while s[head] == " ":
                head-=1
            tail = head
        return " ".join(res)
        