class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        answer=""
        for i in range(len(s)):
            if s[i]=="(":
                if count>0:
                    answer+=s[i]
                count+=1
            else:
                count-=1
                if count>0:
                    answer+=s[i]
        return answer
        