class UnionFind:
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n 

    def find(self,x): 
        # Path compression: make all nodes point to root
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): 
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y: 
            return False 
        
        # Uion by rank: attach smaller tree under larger
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]: 
            self.parent[root_y] = root_x
        else: 
            self.parent[root_y] = root_x
            self.rank[root_x] += 1 

        self.components -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count_components(self): 
        return self.components


