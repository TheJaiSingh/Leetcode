class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        previous=intervals[0][1]
        remove=0
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            if start>=previous:
                previous=end
            else:
                remove+=1
        return remove
            
        