class Solution(object):
    def maxVowels(self, s, k):
        count=0
        vovel="AEIOUaeiou"
        for i in range(k):
            if s[i] in vovel:
                count+=1
        max_vovel=count
        left=0
        for right in range(k,len(s)):
            if s[left] in vovel:
                count-=1
            if s[right] in vovel:
                count+=1
            left+=1
            if count>max_vovel:
                max_vovel=count

        return max_vovel