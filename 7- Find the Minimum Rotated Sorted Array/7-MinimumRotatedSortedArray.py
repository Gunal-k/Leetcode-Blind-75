class Solution:
    def findMin(self,nums:list[int])->int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l<=r :
            if nums[l] < nums[r]:
                res = nums[0]
                break
            
            mid = (l+r) // 2
            res = min(res,nums[mid])
            if nums[l] >= nums[r]:
                l = mid+1
            else:
                r = mid-1
        return res

# test code for algorithm
sol = Solution()
print(sol.findMin([4,5,1,2,3]))