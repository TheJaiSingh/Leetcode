class Solution(object):
    def isIsomorphic(self, s, t):
        map={}
        map2={}
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]]=t[i]
            else:
                if map[s[i]]!=t[i]:
                    return False
            if t[i] not in map2:
                map2[t[i]]=s[i]
            else:
                if map2[t[i]]!=s[i]:
                    return False
            
        return True