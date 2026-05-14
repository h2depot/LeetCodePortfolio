import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] ch_list = s.toCharArray();
        int left = 0;
        int right = 0;
        int max = 0;
        Map<Character, Integer> strs = new HashMap<>();
        while(right < ch_list.length){
            if(strs.containsKey(ch_list[right])){
                left = Math.max(left, strs.get(ch_list[right])+1);
            }
            strs.put(ch_list[right], right);
            max = Math.max(max, right-left+1);
            right++;
        }
        return max;
    }
}