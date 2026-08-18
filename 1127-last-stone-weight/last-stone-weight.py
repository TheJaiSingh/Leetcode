class Solution(object):
    def lastStoneWeight(self, stones):
        def heapify(stones, ind, heap_size):
            largest = ind
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < heap_size and stones[left] > stones[largest]:
                largest = left
            if right < heap_size and stones[right] > stones[largest]:
                largest = right
            if largest != ind:
                stones[ind], stones[largest] = stones[largest], stones[ind]
                heapify(stones, largest, heap_size)

        def build_max(stones):
            n = len(stones)
            for i in range(n // 2 - 1, -1, -1):
                heapify(stones, i, n)

        def maximum(stones):
            max_val = stones[0]
            stones[0] = stones[-1]
            stones.pop()
            if len(stones) > 0:
                heapify(stones, 0, len(stones))
            return max_val

        def insert(stones, value):
            stones.append(value)
            ind = len(stones) - 1
            while ind > 0:
                parent = (ind - 1) // 2
                if stones[ind] > stones[parent]:
                    stones[ind], stones[parent] = stones[parent], stones[ind]
                    ind = parent
                else:
                    break

        build_max(stones)

        while len(stones) > 1:
            y = maximum(stones)
            x = maximum(stones)
            if x != y:
                insert(stones, y - x)

        if len(stones) == 1:
            return stones[0]

        return 0