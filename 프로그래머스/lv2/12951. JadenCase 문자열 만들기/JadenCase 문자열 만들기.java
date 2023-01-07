class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isFirstCharacter = true;
        for(Character c : s.toCharArray()) {
            if(c.equals(' ')) {
                isFirstCharacter = true;
            }
            else if(isFirstCharacter){
                c = Character.toUpperCase(c);
                isFirstCharacter = false;
            }
            else {
                c = Character.toLowerCase(c);
            }
            sb.append(c);
        }
        return sb.toString();
    }
}