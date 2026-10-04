class Solution(object):
    def minInsertions(self, s):

        open = 0
        answer = 0
        i = 0

        while i < len(s):

            if s[i] == '(':

                open += 1

            else:

                if i + 1 < len(s) and s[i + 1] == ')':

                    i += 1

                else:

                    answer += 1

                if open > 0:
                    open -= 1

                else:

                    answer += 1

            i += 1

        answer += open * 2

        return answer