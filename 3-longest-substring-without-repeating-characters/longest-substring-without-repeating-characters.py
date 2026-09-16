class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq={}
        maxlength=0
        left=0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            
            while freq[s[right]]>1:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            window_length=right-left+1
            maxlength=max(maxlength,window_length)
        return maxlength