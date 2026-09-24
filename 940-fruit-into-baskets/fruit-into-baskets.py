class Solution(object):
    def totalFruit(self, fruits):
        left=0
        freq={}
        maxlength=0
        for right in range(len(fruits)):
            if fruits[right] not in freq:
                freq[fruits[right]]=1
            else:
                freq[fruits[right]]+=1

            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            maxlength=max(maxlength,right-left+1)

        return maxlength     