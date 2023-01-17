class Solution {
    boolean[] isVisited;
    int dungeonCount;
    int[][] dungeonsArray;
    int maxExploreCount = 0;
    public int solution(int k, int[][] dungeons) {
        dungeonCount = dungeons.length;
        isVisited = new boolean[dungeonCount];
        dungeonsArray = dungeons;
        exploreDungeons(k, 0);

        return maxExploreCount;
    }

    public void exploreDungeons(int num, int depth) {
        if(dungeonCount == depth) {
            return;
        }
        for(int i = 0; i < dungeonCount; i++) {
            if(isVisited[i]) continue;
            if(num >= dungeonsArray[i][0]) {
                if(maxExploreCount < depth + 1) maxExploreCount = depth + 1;
                isVisited[i] = true;
                exploreDungeons(num - dungeonsArray[i][1], depth + 1);
                isVisited[i] = false;
            }
        }
    }
}