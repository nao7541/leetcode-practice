class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        subsequence = 0
        for i in range(0, len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence] == t[i]:
                    subsequence+=1
        
        return subsequence == len(s)

def main():
    solution = Solution()
    
    # テストケース
    s = "abc"
    t = "ahbgdc"
    expected = True
    
    result = solution.isSubsequence(s, t)
    print(f"Input: s = {s}, t = {t}, Expected: {expected}, Result: {result}")
    assert result == expected, f"Test failed for input: s = {s}, t = {t}"

if __name__ == "__main__":
    main()

# time complexity: O(n)
# space complexity: O(1)