'''
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''

from random import random
class Solution:
    def toss_biased(self, p):
        return int(random() < p)

p = .2
Solution().toss_biased(p)
