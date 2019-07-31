#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(graph, res, visited, i):
            # 在某个顶点的邻接表中重复访问一个节点，说明有环
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True

            visited[i] = -1
            for j in graph[i]:
                if not dfs(graph, res, visited, j):
                    return False
            visited[i] = 1
            res.append(i)
            return True

        if (not isinstance(numCourses, int) or numCourses <= 0
            or not isinstance(prerequisites, list)):
            return False

        visited = [False for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        res = []
        for i in range(numCourses):
            if not dfs(graph, res, visited, i):
                return []
        return res

