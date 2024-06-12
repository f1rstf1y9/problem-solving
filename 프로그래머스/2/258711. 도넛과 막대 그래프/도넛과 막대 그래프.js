function solution(edges) {
    
    let point = 0;
    let donut = 0;
    let bar = 0;
    let eight = 0;
    
    const outNodes = new Map();
    const enterNodes = new Map();
    const vertices = new Set();
    for (const [start, end] of edges) {
        vertices.add(start);
        vertices.add(end);
        
        if (!outNodes.get(start)) {
            outNodes.set(start,[]);
        }
        const value_out = outNodes.get(start);
        value_out.push(end);
        outNodes.set(start, value_out);
    
        if (!enterNodes.get(end)) {
            enterNodes.set(end,[]);
        }
        const value_enter = enterNodes.get(end);
        value_enter.push(start);
        enterNodes.set(end, value_enter);
    }
    
    for (const vertex of vertices) {
        if (!outNodes.get(vertex)) {
            outNodes.set(vertex, []);
        }
        if (!enterNodes.get(vertex)) {
            enterNodes.set(vertex, []);
        }
        const outNodesCount = outNodes.get(vertex).length;
        const enterNodesCount = enterNodes.get(vertex).length;
        
        if (outNodesCount >= 2 && !enterNodesCount) {
            point = vertex;
        }
        else if (!outNodesCount) {
            bar += 1;
        }
        else if (outNodesCount == 2) {
            eight += 1;
        }
    }
    donut = outNodes.get(point).length - bar - eight;
    return [point, donut, bar, eight];
}