class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        val = len(nums)
        for i in range(len(nums)):
            val+= (i-nums[i])
        return val
        
sol = Solution()
print(sol.missingNumber([0,1]))
print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))