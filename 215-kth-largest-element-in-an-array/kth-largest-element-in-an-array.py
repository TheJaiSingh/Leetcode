class Solution(object):
    def findKthLargest(self, nums, k):
        def heapify_down(nums,ind,heap_size):
            largest=ind
            left=2*ind+1
            right=2*ind+2
            if left<heap_size and nums[left]>nums[largest]:
                largest=left
            if right<heap_size and nums[right]>nums[largest]:
                largest=right
            if largest!=ind:
                nums[ind],nums[largest]=nums[largest],nums[ind]
                heapify_down(nums,largest,heap_size)
        def built_max(nums):
            n=len(nums)
            for i in range(n//2-1,-1,-1):
                heapify_down(nums,i,n)
        built_max(nums)
        heap_size=len(nums)
        for i in range(k):
            maximum=nums[0]
            nums[0]=nums[heap_size-1]
            heap_size-=1
            if heap_size>0:
                heapify_down(nums, 0, heap_size)
        return maximum
