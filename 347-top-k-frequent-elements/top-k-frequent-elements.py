class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        output = []

        for i in sorted(freq, key=freq.get, reverse=True):
            output.append(i)

            if len(output) == k:
                break

        return output
