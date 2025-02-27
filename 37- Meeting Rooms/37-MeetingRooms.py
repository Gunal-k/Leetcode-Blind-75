class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeeting(self, intervals):
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
sol = Solution()
print(sol.canAttendMeeting(intervals)) # False