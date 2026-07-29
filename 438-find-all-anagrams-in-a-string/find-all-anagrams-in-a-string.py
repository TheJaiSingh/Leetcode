class Solution(object):
    def findAnagrams(self, s, p):
        arr={}
        for ch in range(len(p)):
            arr[p[ch]]=arr.get(p[ch],0)+1
        left=0
        result=[]
        arr2={}
        for sh in range(len(s)):
            arr2[s[sh]]=arr2.get(s[sh],0)+1
            if sh-left+1>len(p):
                left_char=s[left]
                arr2[left_char]-=1
                if arr2[left_char]==0:
                    del arr2[left_char]
                left+=1
            if sh-left+1==len(p):
                if arr==arr2:
                    result.append(left)
        return result
        