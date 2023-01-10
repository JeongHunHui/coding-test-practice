class Solution {
    boolean solution(String s) {
        int a = 0;
        for(char c : s.toCharArray()) {
            if(c == '(') a++;
            else a--;
            if(a<0) return false;
        }
        if(a != 0) return false;
        return true;
    }
}