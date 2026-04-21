class Solution:
    def climbStairs(self, n: int) -> int:
                   # базовые случаи
        if n <= 2:
            return n

        # dp[i-2] и dp[i-1]
        a, b = 1, 2

        for i in range(3, n + 1):
            # текущее значение
            c = a + b
            a = b
            b = c

        return b