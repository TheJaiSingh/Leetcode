class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result=[]
        start,end=intervals[0]
        for i in range(1,len(intervals)):
            start2,end2=intervals[i]
            if start2<=end:
                start=min(start,start2)
                end=max(end,end2)
            else:
                result.append([start,end])
                start=start2
                end=end2
        result.append([start,end])
        return result
        