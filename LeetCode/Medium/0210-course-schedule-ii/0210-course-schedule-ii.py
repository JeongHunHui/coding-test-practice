from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degrees = [0] * numCourses
        for course, precourse in prerequisites:
            graph[precourse].append(course)
            degrees[course] += 1
        que = deque([i for i in range(numCourses) if degrees[i] == 0])
        answer = []
        while que:
            pre_course = que.popleft()
            answer.append(pre_course)
            for next_course in graph[pre_course]:
                degrees[next_course] -= 1
                if degrees[next_course] == 0:
                    que.append(next_course)
        if len(answer) == numCourses:
            return answer
        return []