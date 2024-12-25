class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        while 0 < num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            ans += 1
        
        return ans

# another solution
class Solution:
    """
    Time:   O(log(n))
    Memory: O(log(n))
    """

    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)