'''
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

class Solution:
    def countMatrixPath(self, n, m):
        res = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]

n, m = 2, 2
n, m = 5, 5
Solution().countMatrixPath(n, m)
