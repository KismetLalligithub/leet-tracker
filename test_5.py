def num_islands(grid): 
    if not grid or not grid[0]: 
        return 0 
    islands = 0 
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    
    def dfs(r, c): 
        if r  >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == '0' or (r, c) in visited: 
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in rows: 
        for c in cols: 
            if grid[r][c] == '1' and (r, c) not in visited: 
                dfs(r, c)
                islands += 1
    return islands
