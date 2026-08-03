class Solution(object):
    def maxProduct(self, nums):
        current_max=nums[0]
        current_min=nums[0]
        answer=nums[0]
        for right in range(1,len(nums)):
            if nums[right]<0:
                current_max,current_min=current_min,current_max
            current_max=max(nums[right],current_max*nums[right])
            current_min=min(nums[right],current_min*nums[right])
            answer=max(answer,current_max)
        return answer