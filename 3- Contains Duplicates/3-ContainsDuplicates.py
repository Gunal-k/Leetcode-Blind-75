class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create a set to keep track of numbers we've seen so far
        seen = set()
        
        # Iterate through each number in the input list
        for i in nums:
            # If the number is already in the set, it's a duplicate
            if i in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(i)
        
        # If no duplicates are found, return False
        return False
        
        # Alternative one-liner (commented out):
        # return len(set(nums)) < len(nums)

# Create an instance of the Solution class
sol = Solution()

# Test the function with an example input
print(sol.containsDuplicate([1, 2, 3, 1]))  # Output: True