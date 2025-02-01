class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:  # Edge case: If prices list is empty, return 0
            return 0

        lPointer = 0  # Left pointer to track the buying day (not needed in final approach)
        minPrice = prices[0]  # Initialize minPrice with the first day's price
        maxProfit = 0  # Initialize maxProfit to 0

        # Optimized approach using minPrice tracking
        for price in prices[1:]:  # Iterate through prices from the second day
            if price < minPrice:  
                minPrice = price  # Update minPrice if a lower price is found
            else:
                maxProfit = max(maxProfit, price - minPrice)  # Calculate and update maxProfit
        
        return maxProfit  # Return the maximum profit found

        # Alternative approach using two pointers
        # rPointer = 1  # Right pointer to track selling day
        # while rPointer < len(prices):
        #     if prices[lPointer] < prices[rPointer]:  
        #         profit = prices[rPointer] - prices[lPointer]  # Calculate profit
        #         maxProfit = max(maxProfit, profit)  # Update maxProfit
        #     else:
        #         lPointer = rPointer  # Move left pointer to the new minimum price index
        #     rPointer += 1  # Move right pointer forward
        # return maxProfit  # Return the maximum profit found

# Create an instance of the Solution class
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected output: 5 (Buy at 1, Sell at 6)
