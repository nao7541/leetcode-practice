class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_rev = list(reversed(s))
        t_rev = list(reversed(t))

        t_dict = {}
        s_idx = []
        for i, n in enumerate(t_rev):
            if n not in t_dict:
                t_dict[n] = [i]
            else:
                t_dict[n].append(i)
        
        for n in s_rev:
            if n not in t_dict:
                return False
            s_idx.append(t_dict[n].pop(0))
            if t_dict[n] == []:
                del t_dict[n]
        
        s_idx_sort = sorted(s_idx)

        if s_idx == s_idx_sort:
            return True
        return False

# Time complexity: O(n)
# Space complexity: O(n)