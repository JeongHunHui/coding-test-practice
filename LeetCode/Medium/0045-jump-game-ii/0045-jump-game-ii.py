class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0 # 점프 수
        end_idx = 0 # jump_count 만큼의 점프로 갈 수 있는 가장 큰 index
        max_idx = 0 # 현재 가장 큰 index
        finish_idx = len(nums)-1
        for i in range(finish_idx):
            # 현재 위치에서 가장 멀리갈 수 있는 위치 업데이트
            max_idx = max(nums[i]+i, max_idx)
            # 현재 위치에서 끝까지 갈 수 있으면 종료
            if max_idx >= finish_idx:
                jump_count += 1
                break
            # 현재 점프 횟수로 갈 수 있는 최대 index에 도착했으면 점프 카운트 증가
            if end_idx == i:
                jump_count += 1
                end_idx = max_idx
        return jump_count