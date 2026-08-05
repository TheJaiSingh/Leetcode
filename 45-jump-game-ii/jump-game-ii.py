class Solution(object):
    def jump(self, nums):
        jump=0
        farthest=0
        current_end=0
        for right in range(len(nums)-1):
            current=right+nums[right]
            farthest=max(farthest,current)
            if right==current_end:
                jump+=1
                current_end=farthest
        return jump
        