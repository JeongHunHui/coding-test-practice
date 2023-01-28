import java.util.Optional;

class Solution {
    String[] cache;
    Integer[] cacheTime;
    int cacheHitTime = 1;
    int defaultTime = 5;
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if(cacheSize <= 0) return cities.length * defaultTime;
        cache = new String[cacheSize];
        cacheTime = new Integer[cacheSize];

        for (int i = 0; i < cities.length; i++) {
            boolean isCacheHit = false;
            String targetString = cities[i];
            for (int j = 0; j < cacheSize; j++) {
                Optional<String> cachedString = Optional.ofNullable(cache[j]);
                if(cachedString.isEmpty()) break;;
                if(cachedString.get().equalsIgnoreCase(targetString)) {
                    isCacheHit = true;
                    cacheTime[j] = i;
                    break;
                }
            }
            if (!isCacheHit) {
                changeCache(targetString, i);
                answer += defaultTime;
            }
            else answer += cacheHitTime;
        }

        return answer;
    }

    void changeCache(String newData, int time) {
        int minTime = Integer.MAX_VALUE;
        int minTimeIndex = 0;
        for (int i = 0; i < cache.length; i++) {
            Optional<String> cachedData = Optional.ofNullable(cache[i]);
            if(cachedData.isEmpty()) {
                minTimeIndex = i;
                break;
            }
            if(cacheTime[i] <= minTime) {
                minTime = cacheTime[i];
                minTimeIndex = i;
            }
        }
        cache[minTimeIndex] = newData;
        cacheTime[minTimeIndex] = time;
    }
}