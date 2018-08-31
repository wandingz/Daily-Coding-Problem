'''
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''

class Solution:
    def LongestPalindromic(self, string):
        if not string:
            return ''

        result = ''
        for i in range(len(string)):
            mcm = self._spreadOut(string, i, i)
            mm = self._spreadOut(string, i, i+1)
            res = (mcm, mm)[len(mcm) < len(mm)]
            result = (result, res)[len(result) < len(res)]
        return result

    def _spreadOut(self, string, l, r):
        while l >=0 and r < len(string) and string[l] == string[r]:
            l -= 1
            r += 1
        return string[l+1:r]

string = 'aabcdcb' # bcdcb
string = 'bananas' # anana
Solution().LongestPalindromic(string)
