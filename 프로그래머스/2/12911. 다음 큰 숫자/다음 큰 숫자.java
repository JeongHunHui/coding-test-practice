class Solution {
    public int solution(int n) {
        int answer = n+1;
        int binaryString1Count = get1Count(n);
        while (binaryString1Count != get1Count(answer)) {
            answer++;
        }
        return answer;
    }

    int get1Count(int num) {
        String binaryString = Integer.toBinaryString(num);
        int count = 0;
        for (char c : binaryString.toCharArray()) {
            if(c == '1') count++;
        }
        return count;
    }
}