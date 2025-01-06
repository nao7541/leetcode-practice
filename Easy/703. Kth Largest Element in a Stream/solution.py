import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        return None

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        if len(self.nums) <= self.k:
            return self.nums[0]
        else:
            heapq.heappop(self.nums)
            return self.nums[0]

# Time complexity: O(nlogk)
# Space complexity: O(k)