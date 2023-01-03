class Solution {
    public static int solution(String s) {
        char[] chars = s.toCharArray();
        int sameCharCount = 0;
        int difCharCount = 0;
        int totalCount = 0;
        char compareChar = ' ';
        for (char c: chars) {
            if(compareChar == ' ') {
                compareChar = c;
                totalCount++;
            }
            if(compareChar == c) {
                sameCharCount++;
            }
            else difCharCount++;
            if(sameCharCount == difCharCount) {
                compareChar = ' ';
                sameCharCount = 0;
                difCharCount = 0;
            }
        }
        return totalCount;
    }
}