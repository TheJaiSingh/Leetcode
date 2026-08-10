class Solution(object):
    def partitionLabels(self, s):
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        result=[]
        start=0
        end=0
        for right in range(len(s)):
            end=max(end,last[s[right]])
            if right==end:
                result.append(end-start+1)
                start=right+1
        return result
        
        