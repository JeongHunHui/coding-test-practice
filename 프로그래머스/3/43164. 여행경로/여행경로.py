from collections import defaultdict

def solution(tickets):
    # key: 출발지, data: {도착지: 티켓 개수}
    ticket_dict = defaultdict(dict)
    for start, end in tickets:
        if end in ticket_dict[start]:
            ticket_dict[start][end] += 1
        else:
            ticket_dict[start][end] = 1
            
    
    ticket_count = len(tickets)
    answers = []
    
    def dfs(airport, path):
        # 모든 티켓을 다 사용했으면 answer에 추가 후 return
        if len(path) == ticket_count+1:
            answers.append(path)
            return
        # 현재 공항에서 갈 수 있는 공항 탐색
        for destination in ticket_dict[airport].keys():
            # 방문 안한 공항이면
            if ticket_dict[airport][destination] >= 1:
                # 방문 처리 후 다음 경로 탐색
                ticket_dict[airport][destination] -= 1
                dfs(destination, path + [destination])
                # 탐색 종료 후 미방문 처리
                ticket_dict[airport][destination] += 1
    
    # 인천 공항부터 탐색
    dfs("ICN", ["ICN"])
    
    # 정답들중 알파뱃이 가장 빠른 답을 반환
    indexes = [i for i in range(len(answers))]
    for i in range(1, ticket_count+1):
        temp_indexes = []
        min_airport = "ZZZZ"
        for index in indexes:
            airport = answers[index][i]
            if airport == min_airport:
                temp_indexes.append(index)
            elif airport < min_airport:
                temp_indexes = [index]
                min_airport = airport
        if len(temp_indexes) == 1:
            return answers[temp_indexes[0]]
        indexes = temp_indexes[:]
    
    return answers[0]