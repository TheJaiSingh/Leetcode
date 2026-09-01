class Solution(object):
    def isSubsequence(self, s, t):
        temp=list(s)
        temp2=list(t)
        left=0
        right=0
        while left<len(s) and right<len(t):
            if temp[left]==temp2[right]:
                left+=1
            right+=1
        if left==len(s):
            return True
        else:
            return False
        