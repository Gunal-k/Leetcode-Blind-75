class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 , rob2 = 0, 0
        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
sol = Solution()
print(sol.rob([2,7,9,3,1])) # 12