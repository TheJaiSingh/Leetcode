class Solution(object):
    def checkValidString(self, s):
        low=0
        high=0
        for i in range(len(s)):
            if s[i]=='(':
                low+=1
                high+=1
            elif s[i]==')':
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            if high<0:
                return False
            low=max(0,low)
        if low==0:
            return True
        else:
            return False
