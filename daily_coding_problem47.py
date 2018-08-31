'''
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

class Solution:
    def MaxProfit(self, stocks):
        if not stocks:
            return

        result = 0
        lowest = stocks[0]
        for x in stocks[1:]:
            if x < lowest:
                lowest = x
            if x > lowest:
                result = max(result, x-lowest)
        return result

stocks = [9, 11, 8, 5, 7, 10]
Solution().MaxProfit(stocks)
