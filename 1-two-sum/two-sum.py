class Solution(object):
    def twoSum(self, nums, target):
        for right in range(len(nums)):
            for left in range(right+1,len(nums)):
                if nums[right]+nums[left]==target:
                    return [right,left]
                    

        