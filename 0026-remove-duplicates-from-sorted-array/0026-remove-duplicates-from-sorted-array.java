class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        int target = nums[k++]; 
        for(int i=1; i<nums.length; i++){
            if(nums[i] != target){
                target = nums[i];
                nums[k] = nums[i];
                k++;
            }else{
                continue;
            }
        }
        return k;
    }
}