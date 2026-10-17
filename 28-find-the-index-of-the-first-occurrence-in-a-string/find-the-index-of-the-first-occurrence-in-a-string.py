class Solution(object):
    def strStr(self, haystack, needle):
        m=len(haystack)
        n=len(needle)
        for left in range(m-n+1):
            right=0
            while right<n and haystack[left+right]==needle[right]:
                right+=1
            if right==n:
                return left
        return -1
        