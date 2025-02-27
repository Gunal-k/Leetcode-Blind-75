class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                res = max(res, count)
                s += 1
            else:
                count -= 1
                e += 1
        return res

intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
sol = Solution()
print(sol.minMeetingRooms(intervals)) # 2