import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> dict = new HashMap<>();
        List<List<String>> ans = new ArrayList<>();
        List<String> keyList = new ArrayList<>();

        for(int i = 0; i < strs.length; i++){
            char[] s = strs[i].toCharArray();
            Arrays.sort(s);
            String sorted = new String(s);
            if(dict.containsKey(sorted) == false){
                dict.put(sorted, new ArrayList<>());
                dict.get(sorted).add(strs[i]);
                keyList.add(sorted);
            }else{
                dict.get(sorted).add(strs[i]);               
            }
        }
        for(String key: keyList){
            ans.add(dict.get(key));
        }
        return ans;
    }
}