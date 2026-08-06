class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If current interval starts before the previous one ends, they overlap
            if intervals[i][0] < prev_end:
                count += 1  # Remove current interval
            else:
                prev_end = intervals[i][1]  # Update end time
                
        return count