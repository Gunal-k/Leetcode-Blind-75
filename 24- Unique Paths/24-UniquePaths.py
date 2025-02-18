class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            
            row = newRow
        
        return row[0]
            

sol = Solution()
print(sol.uniquePaths(3,7)) # 28
print(sol.uniquePaths(3,2)) # 3