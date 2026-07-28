class Solution(object):
    def findMaxAverage(self, nums, k):
        windowsum=0
        maxsum=float("-inf")

        for right in range(len(nums)):
            windowsum+=nums[right]
            if right>=k-1:
                maxsum=max(windowsum,maxsum)
                windowsum-=nums[right-k+1]
        return float(maxsum)/k


