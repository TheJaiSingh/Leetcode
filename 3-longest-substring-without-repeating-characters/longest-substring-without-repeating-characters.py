class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq={}
        max_length=0
        left=0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            length=right-left+1
            if length>max_length:
                max_length=length
        return max_length

