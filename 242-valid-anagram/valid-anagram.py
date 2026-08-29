class Solution(object):
    def isAnagram(self, s, t):
        freq={}
        
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        for i in t:
            if i not in freq:
                return False
                break
            else:
                freq[i]-=1
        for i in freq:
            if freq[i]!=0:
                return False
                break
        else:
            return True
        