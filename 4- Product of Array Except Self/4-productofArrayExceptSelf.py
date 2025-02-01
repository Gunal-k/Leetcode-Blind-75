class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)  # Get the length of the input list
        res = [1] * n  # Initialize result list with 1s
        
        # Calculate prefix products
        prefix = 1  # Variable to store the cumulative product from the left
        for i in range(n):
            res[i] = prefix  # Store the product of all elements before index i
            prefix *= nums[i]  # Update prefix for the next iteration
        
        # Calculate postfix products and multiply with prefix
        postfix = 1  # Variable to store the cumulative product from the right
        for i in range(n-1, -1, -1):  # Iterate from the end to the beginning
            res[i] *= postfix  # Multiply the stored prefix product with the postfix product
            postfix *= nums[i]  # Update postfix for the next iteration
        
        return res  # Return the final result list
