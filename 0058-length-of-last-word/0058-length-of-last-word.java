class Solution {
    public int lengthOfLastWord(String s) {
        boolean isWord = false;
        int cnt = 0;
        for(int i = s.length()-1; i>=0 ; i--){
            if(isWord == false && s.charAt(i) == ' '){
                continue;
            }else if(isWord == true && s.charAt(i) == ' '){
                return cnt;
            }else{
                isWord = true;
                cnt++;
            }
        }
        return cnt;
    }
}