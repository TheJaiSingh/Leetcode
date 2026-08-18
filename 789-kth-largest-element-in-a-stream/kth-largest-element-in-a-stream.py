class KthLargest(object):


    def heapify_down(self, ind):
        n = len(self.heap)

        while True:
            smallest = ind

            left = 2 * ind + 1
            right = 2 * ind + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != ind:
                self.heap[ind], self.heap[smallest] = \
                    self.heap[smallest], self.heap[ind]

                ind = smallest
            else:
                break


    def heapify_up(self, ind):
        while ind > 0:
            parent = (ind - 1) // 2

            if self.heap[ind] < self.heap[parent]:
                self.heap[ind], self.heap[parent] = \
                    self.heap[parent], self.heap[ind]

                ind = parent
            else:
                break


    def insert(self, value):
        self.heap.append(value)

        self.heapify_up(len(self.heap) - 1)


    def minimum(self):
        minimum = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.heapify_down(0)

        return minimum


    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for num in nums:
            self.insert(num)

            if len(self.heap) > self.k:
                self.minimum()


    def add(self, val):
        self.insert(val)

        if len(self.heap) > self.k:
            self.minimum()

        return self.heap[0]