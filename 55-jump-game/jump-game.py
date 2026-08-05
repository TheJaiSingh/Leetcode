class Solution(object):
    def canJump(self, nums):
        farthest=0
        for right in range(len(nums)):
            if right>farthest:
                return False
                break
            current=right+nums[right]
            farthest=max(current,farthest)
        else:
            return True
            
        