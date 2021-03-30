class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i//2 + 1):
                #j * (i-j) -> 如果不切了剩下就是i-j
                # j * dp[i-j] -> 继续切就用dp[i-j]
                dp[i] = max(dp[i], max(j * (i-j) , j * dp[i-j]))
        return dp[n]