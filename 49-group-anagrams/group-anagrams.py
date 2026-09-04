class Solution(object):
    def groupAnagrams(self, strs):
        freq={}
        for i in strs:
            key="".join(sorted(i))
            if  key not in freq:
                freq[key]=[]
            freq[key].append(i)
        return list(freq.values())


  