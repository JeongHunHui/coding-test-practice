class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        l = len(candidates)
        def backtracking(value, record, idx):
            if value >= target:
                if value == target:
                    answer.append(record)
                return
            for i in range(idx, l):
                backtracking(value+candidates[i], record+[candidates[i]], i)
        backtracking(0,[],0)
        return answer
