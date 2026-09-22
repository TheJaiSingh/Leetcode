class Solution(object):
    def longestOnes(self, nums, k):
        left=0
        maxlength=0
        found=0
        for right in range(len(nums)):
            if nums[right]==0:
                found+=1
            while found>k:
                if nums[left]==0:
                    found-=1
                left+=1
            maxlength=max(maxlength,right-left+1)
        return maxlength
