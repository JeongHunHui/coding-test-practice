class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isFirstCharacter = true;
        for(Character c : s.toLowerCase().toCharArray()) {
            sb.append(isFirstCharacter ? Character.toUpperCase(c) : c);
            isFirstCharacter = c.equals(' ');
        }
        return sb.toString();
    }
}