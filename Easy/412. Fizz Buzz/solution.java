class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<String>();
        for (int i = 1; i < n+1; i++){
            if (i % 15 == 0){
                ans.add("FizzBuzz");
            } else if (i % 5 == 0){
                ans.add("Buzz");
            } else if (i % 3 == 0){
                ans.add("Fizz");
            } else {
                ans.add(Integer.toString(i));
            }
        }
        return ans;
    }
}

// another solution
// 三項演算子を使って、FizzBuzz問題を解く
class Solution {
    public List fizzBuzz(int n) {
        List ans = new ArrayList<>();
        for(int i = 1; i <= n; i++){
            ans.add(
                i % 15 == 0 ? "FizzBuzz" :
                i % 5 == 0  ? "Buzz" :
                i % 3 == 0  ? "Fizz" :
                String.valueOf(i)
            );
        }

        return ans;
    }
}