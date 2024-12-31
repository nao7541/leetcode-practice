class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict_r = {}

        for n in ransomNote:
            if n not in dict_r:
                dict_r[n] = 1
            else:
                dict_r[n] += 1
        
        for k in dict_r.keys():
            if dict_r[k] > magazine.count(k):
                return False
        
        return True

# Time complexity: O(n)
# Space complexity: O(n)