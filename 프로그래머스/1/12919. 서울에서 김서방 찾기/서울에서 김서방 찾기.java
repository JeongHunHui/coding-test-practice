class Solution {
    public String solution(String[] seoul) {
        for(int i = 0; i < seoul.length; i++) {
            String person = seoul[i];
            if(person.equals("Kim")) {
                return "김서방은 " + i + "에 있다";
            }
        }
        return "김서방을 찾을 수 없습니다.";
    }
}