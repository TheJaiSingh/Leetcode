class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)<1:
            return 0
        left=0
        freq={}
        maxsum=float("-inf")
        windowsum=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while freq[s[right]]>1:
                left_char=s[left]
                freq[left_char]-=1
                left+=1
            currentlenght=right-left+1
            maxsum=max(currentlenght,maxsum)
        return maxsum




        