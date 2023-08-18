from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = deque([])
    cache_hit_count = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache_hit_count += 1
            cache.remove(city)
        elif len(cache) >= cacheSize:
            cache.popleft()
        cache.append(city)
    return (len(cities) - cache_hit_count) * 5 + cache_hit_count