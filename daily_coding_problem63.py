'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word:
            return True
        n, m = len(board), len(board[0])

        def _dfs(i, j, k, seen):
            if k == len(word):
                return True

            for x,y in [(i,j+1),(i+1,j)]:
                if x in range(len(board)) and y in range(m):
                    if board[x][y] == word[k] and (x,y) not in seen:
                        seen += (x,y),
                        if _dfs(x, y, k+1, seen):
                            return True
            if seen:
                seen.pop()
            return False

        return any(_dfs(i, j, 1, [(i, j)]) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == word[0])



board = [['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']]
word = 'FOAM'
word = 'MASS'
word = 'SSA'
Solution().exist(board, word)
