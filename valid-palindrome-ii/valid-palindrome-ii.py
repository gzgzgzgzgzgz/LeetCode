class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        front = 0
        end = len(s) - 1
        while front <= end:
            if s[end] == s[front]:
                end -= 1
                front += 1
            else:
                return s[front:end] == s[front:end][::-1] or s[front+1:end+1] == s[front+1:end+1][::-1]
        return True
        