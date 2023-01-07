import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
        List<Integer> numbers = Arrays.asList(s.split(" ")).stream().map(str  -> Integer.parseInt(str)).collect(Collectors.toList());
        int firstNum = numbers.get(0);
        int min = firstNum, max = firstNum;

        for (int i = 1; i < numbers.size(); i++) {
            int num = numbers.get(i);
            if(min > num) min = num;
            else if(max < num) max = num;
        }

        StringBuilder sb = new StringBuilder().append(min).append(" ").append(max);
        return sb.toString();
    }
}