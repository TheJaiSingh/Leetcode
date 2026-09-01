class Solution(object):
    def reverseStr(self, s, k):

        temp = list(s)

        start = 0

        while start < len(s):

            left = start
            right = min(start + k - 1, len(s) - 1)

            while left < right:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1

            start += 2 * k

        output = ""

        for i in temp:
            output += i

        return output