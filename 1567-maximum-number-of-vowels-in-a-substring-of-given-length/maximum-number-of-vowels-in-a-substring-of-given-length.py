class Solution(object):
    def maxVowels(self, s, k):
       vovel="AEIOUaeiou"
       vovel_count=0
       maxsum=float("-inf")
       for right in range(len(s)):
        if s[right] in vovel:
            vovel_count+=1
        if right>=k-1:
            maxsum=max(maxsum,vovel_count)
            left=right-k+1
            if s[left] in vovel:
                vovel_count-=1
       return maxsum