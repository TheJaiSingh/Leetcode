class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix=0
        freq={0:-1}
        for right in range(len(nums)):
            prefix+=nums[right]
            rem=prefix % k
            if rem in freq:
                if right-freq[rem]>=2:# right-freq[rem] === lenght
                    return True
                
            else:
                freq[rem]=right
        else:
            return False
