class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        windowsum=0
        count=0
        for right in range(len(arr)):
            windowsum+=arr[right]
            if right>=k-1:
                average=windowsum/k
                if average>=threshold:
                    count+=1
                windowsum-=arr[right-k+1]
        return count