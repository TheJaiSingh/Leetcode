class Solution(object):
    def characterReplacement(self, s, k):
        left=0
        freq={}
        maxfreq=0
        maxsum=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            maxfreq=max(maxfreq,freq[s[right]])
            while right-left+1-maxfreq>k:
                freq[s[left]]-=1
                left+=1
            currentlength=right-left+1
            maxsum=max(maxsum,currentlength)
        return maxsum     