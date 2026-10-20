class Solution(object):
    def repeatedSubstringPattern(self, s):
        n=len(s)
        lps=[0]*len(s)
        lenght=0
        i=1
        while i<n:
            if s[i]==s[lenght]:
                lenght+=1
                lps[i]=lenght
                i+=1
            elif lenght>0:
                lenght=lps[lenght-1]
            else:
                lps[i]=0
                i+=1
        
        longest=lps[n-1]
        pattern_lenght=n-longest
        if longest>0 and n%pattern_lenght==0:
            return True
        return False