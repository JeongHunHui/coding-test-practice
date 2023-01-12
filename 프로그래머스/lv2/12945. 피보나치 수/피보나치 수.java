class Solution {
    final int divideNum = 1234567;
    public int solution(int n) {
        return fibo2(n);
    }

    public int fibo2(int n) {
        double a = 0;
        double b = 1;
        double newNum = 0;
        int count = 1;
        for (int i = 2; i <= n; i++) {
            newNum = a+b;
            if(newNum >= divideNum) {
                newNum = newNum % divideNum;
                b = b % divideNum;
                count++;
            }
            a = b;
            b = newNum;
        }
        return (int)(newNum);
    }
}