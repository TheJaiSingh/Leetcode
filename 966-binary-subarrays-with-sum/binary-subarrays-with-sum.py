class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix=0
        freq={0:1}
        count=0
        for right in range(len(nums)):
            prefix+=nums[right]
            need=prefix-goal
            if need in freq:
                    count+=freq[need]

            freq[prefix]=freq.get(prefix,0)+1
        return count
        