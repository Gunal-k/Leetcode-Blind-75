class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0,len(height)-1
        max_area = 0
        while l<r:
            max_area = max(min(height[l],height[r] )* (r-l),max_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

sol = Solution()
heights_1 = [1,8,6,2,5,4,8,3,7]
heights_2 = [1,1]
print(sol.maxArea(heights_1))
print(sol.maxArea(heights_2))