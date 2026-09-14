class Solution(object):
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        freq={}
        for i in range(len(p)):
            if s[i] not in freq:
                freq[s[i]]=1
            else:
                freq[s[i]]+=1
        freq2={}
        for i in p:
            if i not in freq2:
                freq2[i]=1
            else:
                freq2[i]+=1
        output=[]
        if freq==freq2:
            output.append(0)
        left=0
        start=len(p)
        for right in range(start,len(s)):
            if s[left] in freq:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            left+=1


            if freq==freq2:
                output.append(left)
        return output