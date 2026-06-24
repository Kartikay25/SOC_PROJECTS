from collections import deque
 
 
def flood_fill_capture(grid, player_id, rows, cols):

    visited = [[False] * cols for _ in range(rows)]
 
    queue = deque()
 
    for r in range(rows):
        for c in range(cols):
            on_edge = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
            if not on_edge:
                continue
 
            is_mine = (grid[r][c] == player_id or grid[r][c] == -player_id)
            if not is_mine and not visited[r][c]:
                visited[r][c] = True
                queue.append((r, c))
 
    four_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
    while queue:
        r, c = queue.popleft()
 
        for dr, dc in four_directions:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if visited[nr][nc]:
                continue
 
            is_mine = (grid[nr][nc] == player_id or grid[nr][nc] == -player_id)
            if is_mine:
                continue
 
            visited[nr][nc] = True
            queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                grid[r][c] = player_id
 
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == -player_id:
                grid[r][c] = player_id
