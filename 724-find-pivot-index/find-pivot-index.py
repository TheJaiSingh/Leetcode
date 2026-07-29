class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        leftsum=0
        for right in range(len(nums)):
            rightsum=total-leftsum-nums[right]
            if leftsum==rightsum:
                return right
            leftsum+=nums[right]
        return -1
        
        
        