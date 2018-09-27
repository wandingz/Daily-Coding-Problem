'''
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

import heapq
class Solution:
    def largestProducBySort(self, nums):
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[-1]
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

    def largestProducByHeapq(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], b[0]*b[1]*a[0])

nums = [-10, -10, 5, 2]
Solution().largestProducByHeapq(nums)
