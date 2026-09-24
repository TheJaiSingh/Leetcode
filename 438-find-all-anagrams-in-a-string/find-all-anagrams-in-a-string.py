class Solution(object):
    def findAnagrams(self, s, p):
        freq={}
        for right in range(len(p)):
            if p[right] not in freq:
                freq[p[right]]=1
            else:
                freq[p[right]]+=1
        window={}
        left=0
        output=[]
        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]]=1
            else:
                window[s[right]]+=1
            
            windowlength=right-left+1
            if windowlength>len(p):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1

            if window==freq:
                output.append(left)

        return output
        