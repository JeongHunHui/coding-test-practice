class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h번 인용된 논문이 h개 이상일 때 h의 최댓값 구하기
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i+1:
                return i
        return len(citations)