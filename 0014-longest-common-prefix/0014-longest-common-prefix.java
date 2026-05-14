import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String a = strs[0];
        String b = strs[strs.length-1];
        String prefix = "";
        int i = 0;
        while(i < a.length() && i < b.length()){
            if(a.charAt(i) != b.charAt(i)){
                break;
            }
            i++;
        }
        prefix = a.substring(0, i);
        return prefix;
    }
}