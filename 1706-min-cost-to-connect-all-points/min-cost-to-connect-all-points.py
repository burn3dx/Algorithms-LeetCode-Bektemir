class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # Массив посещённых вершин
        visited = [False] * n
        # Мини-куча (стоимость, вершина)
        heap = [(0, 0)]
        result = 0
        edges_used = 0
        while edges_used < n:
            cost, i = heapq.heappop(heap)
            if visited[i]:
                continue
            visited[i] = True
            result += cost
            edges_used += 1
            # Добавляем рёбра ко всем другим вершинам
            for j in range(n):
                if not visited[j]:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    # Манхэттенское расстояние
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(heap, (dist, j))
        return result