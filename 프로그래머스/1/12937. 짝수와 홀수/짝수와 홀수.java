class Solution {
    public String solution(int num) {
        if(num < 0) num *= -1;
        if(num == 0) return "Even";
        if(num % 2 == 1) return "Odd";
        return "Even";
    }
}