class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int min = nums.length+1;
        int sum = 0;
        for (right = 0; right < nums.length; right++){
            sum += nums[right];
                while(sum >= target){
                    min = Math.min(min, right-left+1);
                    sum -= nums[left];
                    left++;
                }
        }
        return min == nums.length+1 ? 0 : min;
    }
}