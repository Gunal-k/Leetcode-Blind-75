class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Sort the input list to make it easier to avoid duplicates and use two pointers
    
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # Skip duplicate elements to avoid duplicate triplets
                continue
            l, r = i + 1, len(nums) - 1  # Initialize two pointers
    
            while l < r:
                sum = a + nums[l] + nums[r]  # Calculate the sum of the triplet
    
                if sum < 0:
                    l += 1  # Move the left pointer to the right to increase the sum
    
                elif sum > 0:
                    r -= 1  # Move the right pointer to the left to decrease the sum
                
                else:
                    res.append([a, nums[l], nums[r]])  # Found a valid triplet
                    l += 1  # Move the left pointer to the right to find the next potential triplet
    
                    while nums[l] == nums[l - 1] and l < r:  # Skip duplicate elements
                        l += 1
        return res

sol = Solution()
print(sol.threeSum([-3, 3, 4, -3, 1, 2]))  # Example test case
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Example test case