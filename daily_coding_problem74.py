'''
This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
'''

class Solution:
    def countOccurrenceTraversal(self, N, X):
        if not N or not X:
            return 0

        count = 0
        for i in range(N):
            for j in range(N):
                if (i+1) * (j+1) == X:
                    count += 1
        return count

    def countOccurrenceSquaring(self, N, X):
        if not N or not X:
            return 0

        count, i = 0, 1
        while i <= X**(1/2):
            if X % i == 0:
                if i == X**(1/2):
                    count += 1
                else:
                    count += (i <= N and X/i <= N) * 2
            i += 1
        return count


N, X = 6, 12
N, X = 10, 36
Solution().countOccurrenceTraversal(N, X)
Solution().countOccurrenceSquaring(N, X)
