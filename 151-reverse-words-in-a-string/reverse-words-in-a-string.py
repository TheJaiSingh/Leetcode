class Solution(object):
    def reverseWords(self, s):
        word=""
        words=[]
        for i in s:
            if i!=" ":
                word+=i
            else:
                if word!="":
                    words.append(word)
                    word=""
        if word!="":
            words.append(word)
        result=""
        for i in range(len(words)-1,-1,-1):
            result+=words[i]
            if i!=0:
                result+=" "

        return result