class NumArray(object):

    def __init__(self, nums):

        self.prefix = []
        count = 0

        for i in range(len(nums)):
            count += nums[i]
            self.prefix.append(count)

    def sumRange(self, left, right):

        if left == 0:
            answer = self.prefix[right]
        else:
            answer = self.prefix[right] - self.prefix[left - 1]

        return answer