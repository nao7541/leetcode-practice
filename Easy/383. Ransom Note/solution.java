public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        String magazine_1 = magazine;
        String magazine_2 = magazine;

        for(int i=0; i<ransomNote.length(); i++){
            magazine_2 = magazine_2.replaceFirst(String.valueOf(ransomNote.charAt(i)), "");
            if(magazine_1.equals(magazine_2)){
                return false;
            } else{
                magazine_1 = magazine_2;
            }
        }

        return true;


    }
} {
    
}

// Time Complexity: O(n^2)
// Space Complexity: O(n)

// other solution

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> magazineLetters = new HashMap<>(); // k = 26

        for (int i = 0; i < magazine.length(); i++) {
            char m = magazine.charAt(i);

            int currentCount = magazineLetters.getOrDefault(m, 0);
            magazineLetters.put(m, currentCount + 1);
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            char r = ransomNote.charAt(i);

            int currentCount = magazineLetters.getOrDefault(r, 0);

            if (currentCount == 0) {
                return false;
            }

            magazineLetters.put(r, currentCount - 1);
        }

        return true;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)
