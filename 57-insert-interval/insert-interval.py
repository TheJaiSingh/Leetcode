class Solution(object):
    def insert(self, intervals, newInterval):
        start,end=newInterval
        result=[]
        for i in range(len(intervals)):
            start2,end2=intervals[i]
            if end2<start:  # before case
                result.append([start2,end2])
            elif start2>end:
                result.append([start,end])
                return result + intervals[i:]
            else:
                start=min(start,start2)
                end=max(end,end2)
        result.append([start,end])
        return result
        
        