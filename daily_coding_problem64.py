'''
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
'''

class Solution:
    pass



class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return nums


nums = [1,1,2]
Solution().removeDuplicates(nums)
