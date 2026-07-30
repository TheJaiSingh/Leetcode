class Solution(object):
    def subarraySum(self, nums, k):
        prefix=0
        count=0
        freq={0:1}
        for right in range(len(nums)):
            prefix+=nums[right]
            if prefix-k in freq:
                count+=freq[prefix-k]
            freq[prefix]=freq.get(prefix,0)+1
        return count
