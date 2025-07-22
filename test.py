def numIslands(grid): 
    if not grid or not grid[0]:
        return 0 

    rows, cols = len(grid), len(grid[0])
    islands = 0 
    seen = set()

    def dfs(r, c): 
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen or grid[r][c] == '0': 
            return 
        seen.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows): 
        for c in range(cols): 
            if grid[r][c] == '1' and (r, c) not in seen: 
                dfs(r, c)
                islands += 1 
    return islands
