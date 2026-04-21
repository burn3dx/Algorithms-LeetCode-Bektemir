class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  # dp[i-1]
        prev2 = 0  # dp[i-2]

        for num in nums:
            # выбираем максимум
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp

        return prev1    