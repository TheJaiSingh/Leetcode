class Solution(object):
    def strStr(self, haystack, needle):
        n=len(haystack)
        m=len(needle)
        if m==0:
            return 0
        lps=[0]*m
        lenght=0
        i=1
        while i<m:
            if needle[i]==needle[lenght]:
                lenght+=1
                lps[i]=lenght
                i+=1
            elif lenght>0:
                lenght=lps[lenght-1]
            else:
                lps[i]=0
                i+=1
        i=0
        j=0
        while i<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==m:
                    return i-j
            elif j>0:
                j=lps[j-1]
            else:
                i+=1
        return -1            
