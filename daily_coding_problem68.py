'''
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
'''

class Solution:
    def chessboard(self, pos):
        if not m or not pos:
            return 0

        bi, fi = 0, 0
        bw, fw = 0, 0
        for i,j in pos:
            if i == j:
                bi += 1
                if bi >= 2:
                    bw += bi-1
            if i + j == m-1:
                fi += 1
                if fi >= 2:
                    fw += fi-1
        return bw + fw

m = 5
pos = [(0, 0),(1, 2),(2, 2),(4, 0)]
Solution().chessboard(pos)
