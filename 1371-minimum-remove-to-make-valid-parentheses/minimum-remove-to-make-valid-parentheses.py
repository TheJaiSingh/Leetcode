class Solution(object):
    def minRemoveToMakeValid(self, s):

        stack = []
        answer = []

        for i in range(len(s)):

            if s[i] == '(':

                stack.append(len(answer))
                answer.append(s[i])

            elif s[i] == ')':

                if len(stack) > 0:
                    stack.pop()
                    answer.append(s[i])

            else:

                answer.append(s[i])

        while len(stack) > 0:

            index = stack.pop()
            answer[index] = ""

        return "".join(answer)