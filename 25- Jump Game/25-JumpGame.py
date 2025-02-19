class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


sol = Solution()
print(sol.canJump([3,2,1,0,4]))  # False
print(sol.canJump([2,3,1,1,4]))  # True