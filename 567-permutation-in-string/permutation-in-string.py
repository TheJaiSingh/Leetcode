
class Solution(object):
    def checkInclusion(self, s1, s2):
        freq = {}
        for i in range(len(s1)):
            if s1[i] not in freq:
                freq[s1[i]] = 1
            else:
                freq[s1[i]] += 1
        window = {}
        left = 0
        for right in range(len(s2)):
            if s2[right] not in window:
                window[s2[right]] = 1
            else:
                window[s2[right]] += 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == freq:
                return True

        return False
