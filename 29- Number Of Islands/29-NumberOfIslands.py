from typing import List
import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc 
                    if (
                        new_r in range(rows) and
                        new_c in range(cols) and
                        grid[new_r][new_c] == "1" and
                        (new_r, new_c) not in visit
                    ):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands

sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # 1