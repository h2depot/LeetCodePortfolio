import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        for(int i = 0;i < nums.length; i++){
            int diff = target - nums[i];
            if (dict.containsKey(diff)){
                return new int[]{dict.get(diff), i};
            }else{
                dict.put(nums[i], i);
            }
        }
        return null;
    }
}