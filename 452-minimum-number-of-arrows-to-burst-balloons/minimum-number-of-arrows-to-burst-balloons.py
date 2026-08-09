class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        count=1
        arrow=points[0][1]
        for i in range(1,len(points)):
            start,end=points[i]
            if start>arrow:
                count+=1
                arrow=end
        return count

        