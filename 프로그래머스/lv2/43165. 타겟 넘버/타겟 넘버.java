class Solution {
    int count = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, 0, "", target);
        return count;
    }

    public void dfs(int[] numbers, int depth, int answer, String str, int target) {
        if(depth == numbers.length) {
            if(answer == target) count++;
            return;
        }
        for (int i = 0; i < 2; i++) {
            int num = i == 0 ? 1 : -1;
            dfs(numbers, depth + 1, answer + numbers[depth] * num, str + num, target);
        }
    }
}