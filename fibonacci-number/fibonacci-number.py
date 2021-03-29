class Solution:
    def fib(self, n: int) -> int:
        if n == 1: return 1
        if n == 0: return 0
        a, b = 0, 1
        for i in range(n):
            a,b = b, a+b
        return a