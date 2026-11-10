class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if not image or image[sr][sc] == color:
        #     return image

        # originalColor = image[sr][sc]
        # image[sr][sc] = color
        # rows = len(image)
        # cols = len(image[0])
        # queue = deque([(sr,sc)])

        # while queue:
        #     r,c = queue.popleft()
        #     for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
        #         nr = dr+r
        #         nc = dc+c
        #         if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == originalColor:
        #             image[nr][nc] = color
        #             queue.append((nr,nc))
        # return image

        if not image or image[sr][sc] == color:
            return image

        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image
