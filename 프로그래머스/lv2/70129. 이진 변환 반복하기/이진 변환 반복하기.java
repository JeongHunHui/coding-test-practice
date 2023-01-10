import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String s) {
        int zeroCount = 0;
        int tryCount = 0;
        while (!s.equals("1")) {
            tryCount++;
            String str = "";
            for(char c : s.toCharArray()) {
                if (c == '0') zeroCount++;
                else str += c;
            }
            s = make01(str.length());
        }
        int[] answer = {tryCount, zeroCount};
        return answer;
    }

    public String make01(int num) {
        int buffer = num;
        String answer = "";
        while (buffer != 1) {
            answer = (buffer % 2) + answer;
            buffer = buffer / 2;
        }
        answer = "1" + answer;
        return answer;
    }
}