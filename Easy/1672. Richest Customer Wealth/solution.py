class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in accounts:
            if ans < sum(i):
                ans = sum(i)
        
        return ans

# 模範解答

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(map(sum, accounts))
        