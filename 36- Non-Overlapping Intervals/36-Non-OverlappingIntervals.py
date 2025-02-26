class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        count=0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count+=1
                prevEnd = min(prevEnd, end)
        return count

sol = Solution()
print(sol.merge([[1,2],[2,3],[3,4],[1,3]])) # 1