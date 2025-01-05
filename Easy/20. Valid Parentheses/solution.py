"""
approach:
  We use a stack to keep track of the opening brackets.
  As we iterate through the string, we push each opening bracket onto the stack.
  For each closing bracket, we check if it matches the most recent opening bracket by popping from the stack.
  If it matches, we continue; otherwise, the string is invalid.
  At the end, if the stack is empty, all the brackets were matched correctly, so the string is valid.
  Otherwise, it is invalid.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = "({["
        bracket_relation = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        bracket_tmp= []

        for n in s:
            if n in opens:
                bracket_tmp.append(n)
            else:
                if len(bracket_tmp) == 0:
                    return False
                if bracket_relation[n] == bracket_tmp[-1]:
                    bracket_tmp.pop(-1)
                else:
                    return False
        if len(bracket_tmp) == 0:
            return True
        else:
            return False

# Time complexity: O(n)
# Space complexity: O(n)