class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix=0
        count=0
        freq={0:1}
        for right in range(len(nums)):
            prefix+=nums[right]
            need=prefix%k
            if need in freq:
                count+=freq[need]
            freq[need]=freq.get(need,0)+1
        return count
                
