class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers
        while l <= r:
            m = (l + r) // 2  # Calculate the middle index
            if target == nums[m]:  # If target is found at the middle index
                return m

            # Check if the left portion is sorted
            if nums[l] <= nums[m]:
                # If target is not in the left sorted portion
                if target < nums[l] or target > nums[m]:
                    l = m + 1  # Move the left pointer to the right of middle
                else:
                    r = m - 1  # Move the right pointer to the left of middle
            
            # If the right portion is sorted
            else:
                # If target is not in the right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m - 1  # Move the right pointer to the left of middle
                else:
                    l = m + 1  # Move the left pointer to the right of middle
        
        return -1  # Return -1 if target is not found

sol = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # Example usage