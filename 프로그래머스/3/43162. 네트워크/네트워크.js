function bfs(queue, computers, visited, n) {
    while (queue.length) {
        const currentComputer = queue.pop();
        const connectedComputers = computers[currentComputer];
        visited[currentComputer] = true;
        for (let connectedComputer = 0; connectedComputer < n; connectedComputer++) {
            if (connectedComputer === currentComputer || !connectedComputers[connectedComputer]) {
                continue;
            }
            if (!visited[connectedComputer]) {
                queue.push(connectedComputer);
            }
        }
    }
}

function solution(n, computers) {
    var answer = 0;
    let visited = new Array(n).fill(false);
    let queue = [];
    
    for (let computer = 0; computer < n; computer++ ) {
        if (!visited[computer]) {
            answer++;
            queue.push(computer);
            bfs(queue, computers, visited, n);
        }
    }
    
    
    return answer;
}