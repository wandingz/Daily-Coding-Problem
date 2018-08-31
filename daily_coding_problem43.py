'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Solution:
    def __init__(self, nums=[]):
        self.heap = [0]
        for v in nums:
            self.heap.append(v)
            self._floatUp(len(self.heap)-1)

    def push(self, v):
        self.heap.append(v)
        self._floatUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap)-1)
            largest = self.heap.pop()
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            largest = self.heap.pop()
        else:
            largest = False
        return largest

    def max(self):
        if self.heap[1]:
            largest = self.heap[1]
        else:
            largest = False
        return largest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatUp(self, i):
        parent = i // 2
        if i == 1:
            return
        else:
            if self.heap[i] > self.heap[parent]:
                self._swap(i, parent)
                self._floatUp(parent)

    def _bubbleDown(self, i):
        l, r = i*2, i*2+1
        t = i
        if len(self.heap) > l:
            t = (t, l)[self.heap[t] < self.heap[l]]
        if len(self.heap) > r:
            t = (t, r)[self.heap[t] < self.heap[r]]
        if t != i:
            self._swap(i, t)
            self._bubbleDown(t)

# [1,2,3]
res = Solution()
res.push(1)
res.max()
res.push(2)
res.push(3)
res.max()
res.pop()
res.heap
res.max()
