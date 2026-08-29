class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq={}
        freq2={}
        for ch in ransomNote:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        for ch in magazine:
            if ch not in freq2:
                freq2[ch]=1
            else:
                freq2[ch]+=1
        for i in freq:
            if i not in freq2:
                return False
            
            if freq[i]>freq2[i]:
                return False
        return True