class Solution(object):
    def totalFruit(self, fruits):
        left=0
        maxsum=float("-inf")
        freq={}
        k=2
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            while len(freq)>k:
                left_char=fruits[left]
                freq[left_char]-=1
                if freq[left_char]==0:
                    del freq[left_char]
                left+=1
            current_lenght=right-left+1
            maxsum=max(current_lenght,maxsum)
        return maxsum
                
