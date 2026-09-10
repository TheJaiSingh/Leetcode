class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        
        left = 0
        max_count = 0
        max_length = 0

        for right in range(len(s)):

            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1

            max_count = max(max_count, freq[s[right]])

            window_length = right - left + 1

            if window_length - max_count > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            window_length = right - left + 1

            if window_length > max_length:
                max_length = window_length

        return max_length