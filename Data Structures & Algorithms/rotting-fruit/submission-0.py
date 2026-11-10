class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        freshFruit = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                if grid[r][c] == 1:
                    freshFruit +=1
        if freshFruit == 0:
            return 0
        
        minutes = 0 
        while queue:
            r,c,min = queue.popleft()
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    freshFruit-=1
                    minutes = min+1
                    queue.append((nr,nc,min+1))
        return minutes if freshFruit == 0 else -1