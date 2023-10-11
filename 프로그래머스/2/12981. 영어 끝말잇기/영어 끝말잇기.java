import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n, String[] words) {
        List<String> wordList = new ArrayList<>();
        Character previousChar = words[0].charAt(words[0].length() - 1);
        wordList.add(words[0]);
        for(int i = 1; i < words.length; i++) {
            String currentWord = words[i];
            if(wordList.contains(currentWord) || !previousChar.equals(currentWord.charAt(0))){
                return new int[]{i%n+1, i/n+1};
            }
            wordList.add(currentWord);
            previousChar = currentWord.charAt(currentWord.length() - 1);
        }
        return new int[]{0,0};
    }
}