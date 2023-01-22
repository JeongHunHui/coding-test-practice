import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(String begin, String target, String[] words) {
        String[] myWords = new String[words.length + 1];
        int targetNumberIndex = -1;
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if(word.equals(target)) targetNumberIndex = i;
            myWords[i] = words[i];
        }
        if(targetNumberIndex == -1) return 0;

        int wordLength = myWords.length;
        int beginNumberIndex = wordLength - 1;
        myWords[beginNumberIndex] = begin;

        boolean[][] isLinked = new boolean[wordLength][wordLength];
        int[] isVisited = new int[wordLength];

        for(int i = 0; i < wordLength; i++) {
            isVisited[i] = -1;
            for (int j = 0; j < wordLength; j++) {
                if(isOneCharDifferent(myWords[i], myWords[j])) isLinked[i][j] = true;
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(beginNumberIndex);
        isVisited[beginNumberIndex] = 0;
        while (queue.size() > 0) {
            int index = queue.poll();
            if(myWords[index].equals(target)) break;
            for (int i = 0; i < wordLength; i++) {
                if(isLinked[index][i] && isVisited[i] == -1) {
                    isVisited[i] = isVisited[index] + 1;
                    queue.add(i);
                }
            }
        }

        return isVisited[targetNumberIndex];
    }

    boolean isOneCharDifferent(String a, String b) {
        boolean isDif = false;
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) != b.charAt(i)) {
                if(isDif) return false;
                isDif = true;
            }
        }
        return isDif;
    }
}