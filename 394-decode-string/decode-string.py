class Solution(object):
    def decodeString(self, s):
        stack=[]
        number=0
        for i in range(len(s)):
            if s[i].isdigit():
                number=number*10+int(s[i])
            elif s[i]=='[':
                stack.append(number)
                stack.append("")
                number=0
            elif s[i]==']':
                string=stack.pop()
                count=stack.pop()
                string=string*count
                if len(stack)>0:
                    stack[-1]+=string
                else:
                    stack.append(string)
            else:
                if len(stack)>0:
                    stack[-1]+=s[i]
                else:
                    stack.append(s[i])
        return stack[0]

        