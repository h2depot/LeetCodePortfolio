import java.util.*;

class Solution {
    public int[] twoSum(int[] numbers, int target) {
      Map<Integer, Integer> dict = new HashMap<>();
      for(int i=0; i < numbers.length; i++){
        int diff = target - numbers[i];
        if(!dict.containsKey(numbers[i])){
            dict.put(diff, i+1);
        }else{
            int[] ans = {dict.get(numbers[i]), i+1};
            return ans;
        }
      }
      return null;
    }
}