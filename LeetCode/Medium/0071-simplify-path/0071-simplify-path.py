class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        currentPath = ''
        for c in path[1:]:
            if c == '/':
                if currentPath == '..':
                    if len(answer) > 0:
                        answer.pop()
                elif currentPath != '.' and currentPath != '':
                    answer.append(currentPath)
                currentPath = ''
                continue
            currentPath += c
        if currentPath == '..':
            if len(answer) > 0:
                answer.pop()
        elif currentPath != '.' and currentPath != '':
            answer.append(currentPath)
        return '/' + '/'.join(answer)