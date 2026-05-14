class Solution {
    public int strStr(String haystack, String needle) {
        System.out.println(haystack.length());
        System.out.println(needle.length());
        for(int i = 0; i < haystack.length() - needle.length()+1; i++){
            String sub = haystack.substring(i, i+needle.length());
            System.out.println(sub);
            if(sub.equals(needle)){
                return i;
            }
        }
        return -1;
    }
}