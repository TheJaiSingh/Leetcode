class Solution(object):
    def threeSumClosest(self, nums, target):
        arr=sorted(nums)
        best_pair=0
        frist_difference=float("inf")
        close=[]
        for i in range(len(arr)-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
            left=i+1
            right=len(arr)-1
            while left<right:
                currentsum=arr[i]+arr[left]+arr[right]
                second_difference=abs(currentsum-target)
                if second_difference<frist_difference:
                    frist_difference=second_difference
                    close=currentsum
               
                elif currentsum==target:
                    break     
                elif currentsum<target:
                    left+=1
                else:
                    right-=1
        return close

            

        