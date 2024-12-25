class Solution {
    public int numberOfSteps(int num) {
        int ans = 0;
        while (num != 0){
            if (num % 2 == 0){
                num /= 2;
            } else {
                num -= 1;
            }
            ans += 1;
        }
        return ans;
    }
}

// Another solution
// 2進数表記で考える
class Solution {
    public int numberOfSteps(int num) {
        int ans = 0;

        while (num > 0){
            if ((num & 1) == 0){ // num: xxxxx0 & bitmask: 000001
                num >>= 1; // 2進数表記で1桁右にずらす(2で割る)
            } else{
                num--;
            }
            ans++;
        }
        return ans;

        // Time Complexity = O(logn)
        // Space Complexity = O(1)
    }
}