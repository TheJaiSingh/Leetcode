class Solution(object):
    def groupAnagrams(self, strs):

        group = {}

        for i in strs:

            key = "".join(sorted(i))

            if key not in group:
                group[key] = []

            group[key].append(i)

        return list(group.values())