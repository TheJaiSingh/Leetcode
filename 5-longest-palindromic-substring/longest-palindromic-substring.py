class Solution(object):
    def longestPalindrome(self, s):

        answer = ""

        for i in range(len(s)):

            for j in range(i, len(s)):

                substring = s[i:j+1]

                if substring == substring[::-1]:

                    if len(substring) > len(answer):
                        answer = substring

        return answer
        