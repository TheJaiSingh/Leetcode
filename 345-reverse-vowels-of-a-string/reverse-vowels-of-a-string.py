class Solution(object):
    def reverseVowels(self, s):
        temp=list(s)
        left=0
        right=len(s)-1
        while left<right:
            if temp[left] not in "AEIOUaeiou":
                left+=1
            elif temp[right] not in "AEIOUaeiou":
                right-=1
            else:
                temp[left],temp[right]=temp[right],temp[left]
                left+=1
                right-=1        
        output=""
        for i in temp:
            output+=i
        return output