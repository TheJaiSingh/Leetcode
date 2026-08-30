class Solution(object):
    def compress(self, chars):
        result=""
        count=1
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                count+=1
            else:
                result+=chars[i]
                if count>1:
                    result+=str(count)

                count=1
        result+=chars[-1]
        if count>1:
            result+=str(count)
        for i in range(len(result)):
            chars[i]=result[i]
        return len(result)        
        
        