class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        visited = set()

        start = [0,0]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r,c)

        queue = deque([start])
        visited.add(start)

        while queue:
            r,c = queue.popleft()
            perim = 4
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    perim -=1
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            total += perim
        return total
        