class Solution(object):
    def findMaxAverage(self, nums, k):
        
        # First window
        window_sum = 0
        
        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum
        
        left = 0
        
        # Slide the window
        for right in range(k, len(nums)):
            
            window_sum -= nums[left]
            window_sum += nums[right]
            
            left += 1
            
            max_sum = max(max_sum, window_sum)
        
        return float(max_sum) / k