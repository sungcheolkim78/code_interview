from typing import List


class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0

                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for i in range(len(graph)):
            if i not in visited:
                if self.check(graph, i, visited) == False:
                    return False
        return True

    def check(self, graph, start, visited):
        q = [(start, 1)]
        while q:
            pop, color = q.pop(0)
            if pop in visited:
                if visited[pop] != color:
                    return False
                continue
            visited[pop] = color

            for v in graph[pop]:
                q.append((v, -color))
        return True


if __name__ == '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    solution = Solution()
    print(solution.isBipartite(graph))

    graph = [[1,3],[0,2],[1,3],[0,2]]
    print(solution.isBipartite(graph))
