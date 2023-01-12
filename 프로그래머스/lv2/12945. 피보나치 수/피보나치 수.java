class Solution {
    public int solution(int n) {
        int a = 0;
        int b = 1;
        int newNum = 0;
        for (int i = 2; i <= n; i++) {
            newNum = (a + b) % 1234567;
            a = b;
            b = newNum;
        }
        return newNum;
    }
}