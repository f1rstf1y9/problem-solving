function solution(k, dungeons) {
    let maxVisited = 0;
    const dungeonsCount = dungeons.length;
    
    const backtracking = (currentK, visited, visitedCount) => {
        maxVisited = Math.max(maxVisited, visitedCount);
        
        if (visited.length == dungeonsCount || currentK <= 0) return;
        
        let currentVisited = false;
        for (let i = 0; i < dungeonsCount; i++ ) {
            const dungeon = dungeons[i];
            if (!visited.includes(i) && currentK >= dungeon[0]) {
                currentVisited = true;
                visited.push(i);
                backtracking(currentK-dungeon[1], visited, visitedCount+1);
                visited.pop();
            }
        }
        if (!currentVisited) return;
    }
    
    backtracking(k, [], 0);
    
    return maxVisited;
}