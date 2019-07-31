#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(graph, visited, i):
            # 在某个顶点的邻接表中重复访问一个节点，说明有环
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True

            visited[i] = -1
            for j in graph[i]:
                if not dfs(graph, visited, j):
                    return False
            visited[i] = 1
            return True

        if (not isinstance(numCourses, int) or numCourses <= 0
            or not isinstance(prerequisites, list)):
            return

        visited = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        # 建立邻接表，对于每一个顶点vi，将邻接于vi的所有顶点vj构成一个单链表或集合
        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not dfs(graph, visited, i):
                return False
        return True

