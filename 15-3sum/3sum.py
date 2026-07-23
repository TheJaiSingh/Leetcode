class Solution(object):
    def threeSum(self, nums):
        arr=sorted(nums)
        target=0
        best_pair=[]
        for i in range(len(arr)-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
            left=i+1
            right=len(arr)-1
            while left<right:
                currentsum=arr[i]+arr[left]+arr[right]
                if currentsum==target:
                    best_pair.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
                elif currentsum<target:
                    left+=1
                else:
                    right-=1
        return best_pair
