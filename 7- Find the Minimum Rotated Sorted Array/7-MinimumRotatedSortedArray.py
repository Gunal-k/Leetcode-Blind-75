class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Initialize the result with the first element of the array
        res = nums[0]
        # Set the left and right pointers
        l, r = 0, len(nums) - 1
        
        # Binary search loop
        while l <= r:
            # If the subarray is already sorted, update the result and break
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # Calculate the middle index
            mid = (l + r) // 2
            # Update the result with the minimum value found so far
            res = min(res, nums[mid])
            
            # Determine which half to continue the search in
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res

# Test code for the algorithm
sol = Solution()
print(sol.findMin([5, 1, 2, 3, 4]))  # Output: 1