from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # key: 선 이수 과목, value: key를 이수한 뒤 들을 수 있는 과목들
        graph = defaultdict(list)
        # 각 과목의 선 이수 과목 수
        in_degree = [0] * numCourses
        # 그래프, 선 이수 과목 수 데이터 세팅
        for n_course, p_course in prerequisites:
            graph[p_course].append(n_course)
            in_degree[n_course] += 1

        # 선 이수 과목이 없는 과목들을 큐에 넣음
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 수료한 과목 수
        completed_courses = 0
        # BFS
        while queue:
            course = queue.popleft()
            completed_courses += 1
            # course를 수료한 뒤 들을 수 있는 과목 탐색
            for n_course in graph[course]:
                # n_course 수료 후 degree 1 감소
                in_degree[n_course] -= 1
                # 모든 선 이수 과목을 수료했다면, 해당 과목을 큐에 추가
                if in_degree[n_course] == 0:
                    queue.append(n_course)

        # 수료한 과목 수와 전체 과목 수가 같으면 True
        return completed_courses == numCourses