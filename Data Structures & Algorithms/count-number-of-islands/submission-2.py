class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return
        # count = 0
        # rows = len(grid)
        # cols = len(grid[0])

        # def dfs(r,c):
        #     if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != '1':
        #         return
        #     grid[r][c] = '#'
        #     dfs(r+1,c)
        #     dfs(r,c+1)
        #     dfs(r-1,c)
        #     dfs(r,c-1)
        
        # for rr in range(rows):
        #     for cc in range(cols):
        #         if grid[rr][cc] == '1':
        #             count+=1
        #             dfs(rr,cc)
        # return count
        if not grid:
            return
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = '#'
            while queue:
                row,col = queue.popleft()
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr,nc = row+dr, col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        queue.append((nr,nc))
                        grid[nr][nc] = '#'
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count+=1
                    bfs(r,c)
        return count








