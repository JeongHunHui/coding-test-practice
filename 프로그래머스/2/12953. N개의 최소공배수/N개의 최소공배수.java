class Solution {
    public int solution(int[] arr) {
        int answer = arr[0] * arr[1] / getNum(arr[0], arr[1]);
        for(int i = 2; i < arr.length; i++) {
            answer = answer * arr[i] / getNum(answer, arr[i]);
        }
        return answer;
    }

    public int getNum(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}