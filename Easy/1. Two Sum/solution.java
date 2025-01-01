class Solution {
  public int[] twoSum(int[] nums, int target) {
      Map<Integer, Integer>numToIndex = new HashMap<>();

      for (int i=0; i < nums.length; i++){
          if (numToIndex.containsKey(target - nums[i])){
              int[] ans = {numToIndex.get(target-nums[i]), i};
              return ans;
          } else {
              numToIndex.put(nums[i], i);
          }
      }
      return null;
  }
}

// Time Complexity: O(n)
// Space Complexity: O(n)