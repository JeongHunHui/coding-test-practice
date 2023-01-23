class Solution
{
    public int solution(int n, int a, int b)
    {
        int roundNum = 0;
        for(int i = 1; n > i; i*=2) {
            roundNum++;
        }

        for (int i = roundNum; i > 0; i--) {
            int middleNum = (int)Math.pow(2, i-1);
            if(a > middleNum) {
                if(b <= middleNum) return i;
                a -= middleNum;
                b -= middleNum;
            }
            else if(b > middleNum) {
                if(a <= middleNum) return i;
                a -= middleNum;
                b -= middleNum;
            }
        }

        return 0;
    }
}