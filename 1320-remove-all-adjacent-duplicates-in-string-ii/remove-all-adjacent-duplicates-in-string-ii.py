class Solution(object):
    def removeDuplicates(self, s, k):
        stack=[]
        for i in range(len(s)):
            if len(stack)>0 and stack[-1][0]==s[i]:
                stack[-1][1]+=1
            else:
                stack.append([s[i],1])
            if stack[-1][1]==k:
                stack.pop()
        answer=""
        for i in range(len(stack)):
            answer+=stack[i][0]*stack[i][1]
        return answer