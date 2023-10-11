class Solution {
    public long solution(int n) {
        final int divideNum = 1234567;
        int previousNum = 1;
        int nextNum = 1;
        for(int i = 1; i < n; i++) {
            int temp = previousNum;
            previousNum = nextNum;
            nextNum += temp;
            if(nextNum >= divideNum) nextNum %= divideNum;
        }
        return nextNum;
    }
}