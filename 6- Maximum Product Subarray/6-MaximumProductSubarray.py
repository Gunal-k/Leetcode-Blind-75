class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Initialize the maximum subarray product with the maximum value in nums
        maxSub = max(nums)
        # Initialize current minimum and maximum products to 1
        currMin, currMax = 1, 1

        for num in nums:
            # If the current maximum product is 0, reset current min and max products to 1
            if currMax == 0:
                currMin, currMax = 1, 1
                continue
            # Temporarily store the current maximum product multiplied by the current number
            tmp = currMax * num
            # Update the current maximum product
            currMax = max(num * currMax, num * currMin, num)
            # Update the current minimum product
            currMin = min(tmp, num * currMin, num)
            # Update the maximum subarray product
            maxSub = max(maxSub, currMax)
        return maxSub

sol = Solution()
# Print the result of the maxProduct method with the given list
print(sol.maxProduct([-2,3,-4]))