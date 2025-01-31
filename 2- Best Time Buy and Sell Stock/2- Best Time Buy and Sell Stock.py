class Solution:
    def maxProfit(self,prices : list[int])->int:
        lPointer, rPointer = 0, 1
        maxProfit = 0
        while rPointer < len(prices):
            if prices[lPointer] < prices[rPointer]:
                profit = prices[rPointer] - prices[lPointer]
                maxProfit = max(maxProfit, profit)
            else:
                lPointer = rPointer
            rPointer += 1
        return maxProfit
sol = Solution()
print(sol.maxStock([7,1,5,3,6,4]))
