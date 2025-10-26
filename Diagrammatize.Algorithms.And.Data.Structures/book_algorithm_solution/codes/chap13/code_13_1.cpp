// 在图G中，从顶点s开始进行搜索
void search(const Graph &G, int s) {
    int N = (int)G.size();  // 图的顶点数

    // 用于图搜索的数据结构
    vector<bool> seen(N, false);    // 初始化所有顶点为未被访问
    queue<int> todo;    // 空状态（对于深度优先搜索，使用stack<int>）

    // 初始化条件
    seen[s] = true; // 将s标记为已被访问
    todo.push(s);   // todo仅包含s

    // 进行搜索，直到todo为空
    while (!todo.empty()) {
        // 从todo中取出一个顶点
        int v = todo.front();
        todo.pop();

        // 查看v可以到达的所有顶点
        for (int x : G[v]) {
            // 不再搜索已经访问的顶点
            if (seen[x]) continue;

            // 将新的顶点x标记为已被访问，并放入todo集合
            seen[x] = true;
            todo.push(x);
        }
    }
}
