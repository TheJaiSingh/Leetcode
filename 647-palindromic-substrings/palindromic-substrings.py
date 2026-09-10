class Solution:
    def countSubstrings(self, s):
        n = len(s)
        result = 0

        # Expand around each possible center
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

        return result
