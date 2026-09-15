class Solution(object):
    def findMaxAverage(self, nums, k):
        windowsum=0
        for i in range(k):
            windowsum+=nums[i]
        maxsum=windowsum
        left=0
        for right in range(k,len(nums)):
            windowsum-=nums[left]
            windowsum+=nums[right]
            left+=1
            maxsum=max(windowsum,maxsum)
        return float(maxsum)/k
        
        