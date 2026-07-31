class Solution(object):
    def findMaxLength(self, nums):
        prefix=0
        longest=0
        freq={0:-1}
        for right in range(len(nums)):
            if nums[right]==0:
                prefix+=-1
            else:
                prefix+=1
            
            if prefix in freq:
                lenght=right-freq[prefix]
                longest=max(longest,lenght)
            else:
                freq[prefix]=right
        return longest
        
        
        