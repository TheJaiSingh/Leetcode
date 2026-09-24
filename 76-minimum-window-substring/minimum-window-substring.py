class Solution(object):
    def minWindow(self, s, t):

        freq = {}

        for ch in t:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        window = {}

        left = 0
        formed = 0

        minlength = float("inf")
        start = 0

        requirement = len(freq)

        for right in range(len(s)):

            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            if s[right] in freq:
                if window[s[right]] == freq[s[right]]:
                    formed += 1

            while formed == requirement:

                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    start = left

                window[s[left]] -= 1

                if s[left] in freq:
                    if window[s[left]] < freq[s[left]]:
                        formed -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

        if minlength == float("inf"):
            return ""

        return s[start:start + minlength]