class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        l = len(values)
        c_dict = dict()
        num = 0
        for e1, e2 in equations:
            if e1 not in c_dict:
                c_dict[e1] = num
                num += 1
            if e2 not in c_dict:
                c_dict[e2] = num
                num += 1
        graph = [[None] * num for _ in range(num)]
        for i, value in enumerate(values):
            n1, n2 = c_dict[equations[i][0]], c_dict[equations[i][1]]
            graph[n1][n2] = value
            graph[n2][n1] = 1/value
        
        answer = None
        def dfs(current,dest,visited_nodes,total):
            nonlocal answer
            if current == dest:
                answer = total
                return
            if answer:
                return
            for i, val in enumerate(graph[current]):
                if i in visited_nodes or not graph[current][i]:
                    continue
                print(i,dest,visited_nodes|{i},total,val)
                dfs(i,dest,visited_nodes|{i},total*val)

        answers = []
        for q1, q2 in queries:
            if q1 not in c_dict or q2 not in c_dict:
                answers.append(-1.0)
                continue
            n1, n2 = c_dict[q1], c_dict[q2]
            dfs(n1, n2, set(), 1)
            if not answer:
                answers.append(-1.0)
                continue
            answers.append(answer)
            answer = None
        return answers