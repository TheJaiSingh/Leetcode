class Solution(object):
    def minWindow(self, s, t):

        # Frequency of characters required from t
        need = {}

        for ch in t:
            if ch not in need:
                need[ch] = 1
            else:
                need[ch] += 1

        # Frequency of characters in current window
        window = {}

        left = 0

        # Number of required characters satisfied
        formed = 0

        # Number of different required characters
        required = len(need)

        # Store minimum window
        minlength = float("inf")
        start = 0

        for right in range(len(s)):

            # Add current character to window
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            # Check whether this required character is satisfied
            if s[right] in need:
                if window[s[right]] == need[s[right]]:
                    formed += 1

            # Window is valid
            while formed == required:

                # Check if current window is smaller
                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    start = left

                # Remove left character
                window[s[left]] -= 1

                # If removing it makes the window invalid
                if s[left] in need:
                    if window[s[left]] < need[s[left]]:
                        formed -= 1

                # Delete zero-frequency character
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

        # No valid window found
        if minlength == float("inf"):
            return ""

        return s[start:start + minlength]