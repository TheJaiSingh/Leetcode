class Solution(object):
    def frequencySort(self, s):

        freq = {}

        for i in s:

            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        output = ""

        for i in sorted(freq, key=freq.get, reverse=True):

            if freq[i] > 1:
                output += i * freq[i]

            elif freq[i] == 1:
                output += i

        return output