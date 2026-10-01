class Solution(object):
    def backspaceCompare(self, s, t):
        stack=[]
        for i in range(len(s)):
            if s[i]!="#":
                stack.append(s[i])
            else:
                if len(stack)>0:
                    stack.pop()
        

        stack2=[]
        for i in range(len(t)):
            if t[i]!="#":
                stack2.append(t[i])
            else:
                if len(stack2)>0:
                    stack2.pop()
        if stack==stack2:
            return True
        else:
            return False