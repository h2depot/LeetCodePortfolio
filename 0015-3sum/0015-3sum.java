import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> ans = new HashSet<>();
        for(int i=0; i< nums.length; i++){
            Map<Integer, Integer> dict = new HashMap<>();
            int target = -1* nums[i];
            for(int j = i+1; j < nums.length; j++){
                int diff = target - nums[j];
                if(!dict.containsKey(diff)){
                    dict.put(nums[j], j);
                }else{
                    List<Integer> appendList = new ArrayList<Integer>();
                    appendList.add(nums[j]);
                    appendList.add(nums[dict.get(diff)]);
                    appendList.add(nums[i]);

                    Collections.sort(appendList);
                    ans.add(appendList);
                }
            }
        }
        return new ArrayList<>(ans);
    }
}