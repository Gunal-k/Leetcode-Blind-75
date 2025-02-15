class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if i>=len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i,curr,total + candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        
        dfs(0,[],0)

        return res

sol = Solution()
candidates = [2,3,6,7]
target = 7

print(sol.combinationSum(candidates,target)) # [[2,2,3],[7]]
