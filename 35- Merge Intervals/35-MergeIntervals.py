class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd,end)
            else:
                res.append([start,end])
        return res

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]