class Solution(object):
    def minAddToMakeValid(self, s):
        add=0
        open=0
        for i in range(len(s)):
            if s[i]=='(':
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    add+=1
        return add+open
        