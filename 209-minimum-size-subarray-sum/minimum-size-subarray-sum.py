class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        windowsum=0
        minsum=float("inf")
        for right in range(len(nums)):
            windowsum+=nums[right]
            while windowsum>=target:
                currentlength=right-left+1
                minsum=min(minsum,currentlength)
                windowsum-=nums[left]
                left+=1
        if minsum==float("inf"):
            return 0
        else:
            return minsum


        
        