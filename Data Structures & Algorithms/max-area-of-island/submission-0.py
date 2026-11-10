class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxIsland = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    queue = deque([(r,c)])
                    grid[r][c] = 0

                    while queue:
                        rc, cc = queue.popleft()
                        area +=1
                        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                            nr = dr+rc
                            nc = dc+cc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr,nc))
                    maxIsland = max(maxIsland, area)
        return maxIsland