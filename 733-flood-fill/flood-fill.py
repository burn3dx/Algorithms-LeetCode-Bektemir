class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        rows = len(image)
        cols = len(image[0])
        q = deque()
        q.append((sr, sc))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                    q.append((nr, nc))
                    image[nr][nc] = color
        return image     