import java.util.Arrays;

class Solution {
    public int maximumWealth(int[][] accounts) {
        int size = accounts.length;
        int ans = 0;
        for (int i = 0; i < size; i++) {
            if (ans < Arrays.stream(accounts[i]).sum()) {
                ans = Arrays.stream(accounts[i]).sum();
            }
        }

        return ans;
    }
}

// Another solution
class Solution {
    public int maximumWealth(int[][] accounts) {
        int res = 0;
        for(int i =0;i<accounts.length;i++){
            int temp = 0;
            for(int j = 0;j<accounts[i].length;j++){
                temp+=accounts[i][j];
            }
            res = Math.max(res,temp);
        }
        return res;
    }
}