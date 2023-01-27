class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        for (int h = 1; h <= n; h++) {
            int viewCount = 0;
            for(int view : citations) {
                if(view >= h) viewCount++;
                else if(view > h) break;
            }
            if(viewCount >= h) answer = h;
        }
        return answer;
    }
}