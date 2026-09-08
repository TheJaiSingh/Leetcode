class Solution(object):
    def countGoodSubstrings(self, s):
        if len(s)<3:
            return 0
        freq={}
        for i in range(3):
            if s[i] not in freq:
                freq[s[i]]=1
            else:
                freq[s[i]]+=1
        count=0
        if len(freq)==3:
            count+=1

            
        min_freq=min(freq.values())
        left=0
        for right in range(3,len(s)):
            if s[left] in freq:
                freq[s[left]]-=1
                if freq[s[left]] == 0:
                    del freq[s[left]]

            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            left+=1
            if len(freq) == 3:
                count +=1
        return count
        