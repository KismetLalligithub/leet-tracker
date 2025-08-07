class Node: 
    def __init__(self, val, neighbors=[]): 
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node): 
    visited = {}
    def dfs(n):
        if not n: 
            return None
        if n in visited: 
            return visited[n]
        copy = Node(n.val)
        visited[n] = copy
        for neighbor in n.neighbors: 
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)
