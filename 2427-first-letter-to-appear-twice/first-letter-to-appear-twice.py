class Solution(object):
    def repeatedCharacter(self, s):
        freq={}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                return i
        