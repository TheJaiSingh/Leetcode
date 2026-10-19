class Solution(object):
    def targetIndices(self, nums, target):
        output=[]
        sorted=nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                output.append(i)
        return output

        