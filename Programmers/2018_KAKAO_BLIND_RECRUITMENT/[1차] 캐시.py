def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize != 0:
        for city in cities:
            city = city.lower()
        
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                    
                cache.append(city)
                answer += 5
    else:
        answer += len(cities) * 5
                
    return answer