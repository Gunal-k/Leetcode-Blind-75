class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1 , rob2 = 0, 0
        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


sol = Solution()
print(sol.rob([1,2,3,1])) # 4