class Solution(object):
    def totalFruit(self, fruits):
        left=0
        maxsum=0
        freq={}
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            while len(freq)>2:
                left_char=fruits[left]
                freq[left_char]-=1
                if freq[left_char]==0:
                    del freq[left_char]
                left+=1
            currentlength=right-left+1
            maxsum=max(currentlength,maxsum)
        return maxsum

        