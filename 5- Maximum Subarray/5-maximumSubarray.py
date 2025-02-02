class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize the maximum subarray sum with the first element
        maxSub = nums[0]
        # Initialize the current sum to 0
        curSum = 0

        # Iterate through each number in the list
        for num in nums:
            # If the current sum is negative, reset it to 0
            if curSum < 0:
                curSum = 0
            # Add the current number to the current sum
            curSum += num
            # Update the maximum subarray sum if the current sum is greater
            maxSub = max(maxSub, curSum)
        
        # Return the maximum subarray sum
        return maxSub

# Create an instance of the Solution class
sol =  Solution()
# Print the result of the maxSubArray method with the given list
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))