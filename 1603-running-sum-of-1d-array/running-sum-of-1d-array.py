class Solution(object):
    def runningSum(self, nums):
        arr=[0]*len(nums)
        arr[0]=nums[0]
        for right in range(1,len(nums)):
            arr[right]=nums[right]+arr[right-1]
        return arr
        