def numIsIslands(grid): 
    if not grid or not grid[0]: 
        return 0

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)
    water_cells = 0 
    
    def get_index(r, c): 
        return r * cols + c

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(rows): 
        for c in range(cols): 
            if grid[r][c] == '0': 
                water_cells += 1 
                continue

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1'): 
                    uf.union(get_index(r, c), get_index(nr, nc))
    return uf.count_components
