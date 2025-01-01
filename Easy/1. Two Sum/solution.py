class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                if num1 + num2 == target:
                    ans.append(i)
                    ans.append(j)
                    break
            if ans != []:
                break
        return ans

# Time complexity: O(n^2)
# Space complexity: O(1)

# another solution
