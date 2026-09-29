class Solution(object):
    def isValid(self, s):
        stack=[]
        pair={
            ')':'(',
            ']':'[',
            '}':'{',

        }
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                    break
                if stack[-1]!=pair[s[i]]:
                    return False
                    break
                stack.pop()
        else:
            if len(stack)==0:
                return True
            else:
                return False