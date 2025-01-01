class Solution {
  public int firstUniqChar(String s) {
      Map<String, Integer> dic = new HashMap<>();
      int ans = 999999;

      for (int i=0; i<s.length(); i++){
          if (dic.containsKey(String.valueOf(s.charAt(i)))) {
              dic.put(String.valueOf(s.charAt(i)), -1);
          } else {
              dic.put(String.valueOf(s.charAt(i)), i);
          }
      }
      int max_v = -100;
      for (Map.Entry<String, Integer> entry : dic.entrySet()) {
          if (max_v < entry.getValue()) {
              max_v = entry.getValue();
          }
      }
      if (max_v == -1) {
          return -1;
      } else {
          for (Map.Entry<String, Integer> entry : dic.entrySet()) {
              if (entry.getValue() == -1){
                  continue;
              } else if (ans > entry.getValue()) {
                  ans = entry.getValue();
              }
          }
          return ans;
      }
  }
}

// Time Complexity: O(n)
// Space Complexity: O(n)

// other solution
class Solution {
  public int firstUniqChar(String s) {
      HashMap<Character, Integer> mp = new HashMap<>();

      for (char a : s.toCharArray()) {
          mp.put(a, mp.getOrDefault(a, 0) + 1);
      }

      for (int i = 0; i < s.length(); i++) {
          if (mp.get(s.charAt(i)) == 1) {
              return i;
          }
      }
      return -1;
  }
}

