class NumArray(object):

    def __init__(self, nums):
        self.arr=[0]*len(nums)
        self.arr[0]=nums[0]
        for right in range(1,len(nums)):
            self.arr[right]=nums[right]+self.arr[right-1]
        

    def sumRange(self, left, right):
        if left==0:
            return self.arr[right]
        else:
            return self.arr[right]-self.arr[left-1]
        
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)