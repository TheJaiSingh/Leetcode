class Solution(object):
    def maximumSubarraySum(self, nums, k):
        if len(nums)<k:
            return 0
        freq={}
        window_sum=0
        for i in range(k):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
            window_sum+=nums[i]
        max_sum = window_sum if len(freq) == k else 0
        left=0
        for right in range(k,len(nums)):
            freq[nums[left]]-=1
            if freq[nums[left]]==0:
                del freq[nums[left]]
            window_sum-=nums[left]
            left+=1
            if nums[right] not in freq:
                freq[nums[right]]=1
            else:
                freq[nums[right]]+=1
            window_sum+=nums[right]
            if len(freq)==k:
                max_sum = max(max_sum, window_sum)
                
                
        return max_sum

