class Solution(object):
    def maxSubArray(self, nums):
        currentsum=0
        maxsum=float("-inf")
        for right in range(len(nums)):
            currentsum+=nums[right]
            maxsum=max(maxsum,currentsum)
            if currentsum<0:
                currentsum=0
        return maxsum