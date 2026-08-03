class Solution(object):
    def maxSubarraySumCircular(self, nums):
        #max
        currentmax=0
        maxsum=float("-inf")
        for right in range(len(nums)):
            currentmax+=nums[right]
            maxsum=max(maxsum,currentmax)
            if currentmax<0:
                currentmax=0

        #min
        currentmin=0
        minsum=float("inf")
        for right in range(len(nums)):
            currentmin+=nums[right]
            minsum=min(minsum,currentmin)
            if currentmin>0:
                currentmin=0
        
        total=sum(nums)
        
        if maxsum<0:
            return maxsum
        else:
            circular=total-minsum
            return max(maxsum,circular)

        