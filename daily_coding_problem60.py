'''
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
'''

class Solution:
    def canPartition(self, nums):
        n, half = len(nums), sum(nums)>>1
        if sum(nums)%1 or max(nums)>half:
            return False
        seen = {}

        def _dfs(cur, i):
            if cur >= half:
                return cur == half
            if cur not in seen:
                seen[cur] = any(_dfs(cur+nums[j],j) for j in range(i+1,n))
            return seen[cur]

        return not nums or _dfs(nums[0], 0)

nums = [15, 5, 20, 10, 35, 15, 10]
nums = [15, 5, 20, 10, 35]
Solution().canPartition(nums)
