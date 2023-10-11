import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> phoneMap = new HashMap<>();
        for(int i = 0; i < phone_book.length; i++) {
            phoneMap.put(phone_book[i], i);
        }
        
        for(int i = 0; i < phone_book.length; i++) {
            String phoneNumber = phone_book[i];
            for(int j = 1; j < phoneNumber.length(); j++) {
                if(phoneMap.containsKey(phoneNumber.substring(0,j))) {
                    return false;
                }
            }
        }
        return true;
    }
}