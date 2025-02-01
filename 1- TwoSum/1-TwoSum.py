class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}  # Dictionary to store numbers as keys and their indices as values
        
        for i, n in enumerate(nums):  # Iterate over the list with index and value
            diff = target - n  # Calculate the difference needed to reach the target
            
            if diff in hashmap:  # Check if the difference exists in the dictionary
                return [hashmap[diff], i]  # Return the indices of the two numbers
            
            hashmap[n] = i  # Store the number and its index in the dictionary
        
        return  # Return None if no pair is found

# Create an instance of the Solution class
sol = Solution()
print(sol.twoSum([2, 1, 5, 3], 4))  # Example usage, expected output: [1, 3]
