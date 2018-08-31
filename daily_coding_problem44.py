'''
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''
# O(2n)
class Solution:
    def CountInversions(self, lst):
        if not lst:
            return

        result = 0
        locate = [0] * (max(lst)+1)
        for x in lst:
            locate[x] += 1
            result += sum(locate[x+1:])
        return result

lst = [2, 4, 1, 3, 5] # 3
lst = [5, 4, 3, 2, 1] # 10
Solution().CountInversions(lst)
