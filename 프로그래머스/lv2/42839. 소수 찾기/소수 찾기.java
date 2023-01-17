import java.util.HashSet;
import java.util.Set;

class Solution {
    Set<Integer> set = new HashSet<>();
    char[] arr;
    boolean[] isVisited;
    public int solution(String numbers) {
        int answer = 0;
        arr = numbers.toCharArray();
        isVisited = new boolean[arr.length];

        dfs("", 0);

        return set.size();
    }

    public void dfs(String str, int depth) {
        if(str != "") {
            int num = Integer.parseInt(str);
            if(isPrime(num)) {
                set.add(num);
            }
        }
        if(depth >= arr.length) return;
        for (int i = 0; i < arr.length; i++) {
            if(isVisited[i]) continue;
            isVisited[i] = true;
            dfs(str + arr[i], depth + 1);
            isVisited[i] = false;
        }
    }

    public boolean isPrime(int num) {
        if(num == 1 || num == 0) return false;
        for(int x = 2; x <= Math.sqrt(num); x++) {
            if(num % x == 0) return false;
        }
        return true;
    }
}