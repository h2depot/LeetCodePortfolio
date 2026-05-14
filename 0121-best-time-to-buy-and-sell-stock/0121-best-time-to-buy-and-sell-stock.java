class Solution {
    public int maxProfit(int[] prices) {
        int max_prof = 0;
        int min_day = 0;
        for(int i = 0; i < prices.length; i++){
            min_day = prices[min_day]<prices[i] ? min_day:i;
            max_prof = max_prof > prices[i] - prices[min_day] ? max_prof: prices[i] - prices[min_day];
        }
        return max_prof;
    }
}