import java.util.Stack;

class Solution {
    public int solution(String s) {
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            Stack<Character> stack = new Stack<>();
            for (char c : s.toCharArray()) {
                if(stack.isEmpty()) stack.push(c);
                else if (c == ')' && stack.peek() == '(') stack.pop();
                else if (c == '}' && stack.peek() == '{') stack.pop();
                else if (c == ']' && stack.peek() == '[') stack.pop();
                else stack.push(c);
            }
            if (stack.isEmpty()) answer++;
            s = s.substring(1) + s.charAt(0);
        }
        return answer;
    }
}