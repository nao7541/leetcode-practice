class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ans = 999999
        for i, c in enumerate(s):
            if c in dic:
                dic[c] = -1
            else:
                dic[c] = i
        if max(dic.values()) == -1:
            return -1
        else:
            for n in dic.values():
                if n == -1:
                    continue
                if ans > n:
                    ans = n
            return ans

# Time complexity: O(n)
# Space complexity: O(n)

# another solution
import collections
class Solution(object):
    def firstUniqChar(self, s):
        hset = collections.Counter(s)
        # Traverse the string from the beginning...
        for idx in range(len(s)):
            # If the count is equal to 1, it is the first distinct character in the list.
            if hset[s[idx]] == 1:
                return idx
        return -1       # If no character appeared exactly once...