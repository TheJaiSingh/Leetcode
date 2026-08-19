class Solution(object):
    def relativeSortArray(self, arr1, arr2):
            maxx=max(arr1)
            count=[0]*(maxx+1)
            for num in arr1:
                count[num]+=1
            result=[]
            for num in arr2:
                while count[num]>0:
                    result.append(num)
                    count[num]-=1
            for c in range(maxx+1):
                while count[c]>0:
                    result.append(c)
                    count[c]-=1
            return result
        