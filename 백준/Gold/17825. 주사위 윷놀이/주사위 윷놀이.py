numbers = list(map(int, input().split()))

# 경로별 점수
game_map = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    [10, 13, 16, 19, 25],
    [20, 22, 24, 25],
    [30, 28, 27, 26, 25],
    [25, 30, 35, 40],
    [40, -1]
]

is_token = [[0]*len(game_map[i]) for i in range(6)] # 현재 말이 해당 위치에 있는지 저장
current_positions = [[0,0] for _ in range(4)] # 4개의 말 각각의 위치 저장
is_token[0][0] = 1 

high_score = 0

def backtracking(cur_round, score):
    global high_score
    
    if cur_round == 10:
        high_score = max(high_score, score)
        return
        
    dice_number = numbers[cur_round]
    visited_pos = []

    for moving_token in range(4):
        way, count = current_positions[moving_token]
        if [way, count] in visited_pos:
            continue
        visited_pos.append([way, count])
        
        if way == -1:  # 이미 도착한 말
            continue
        
        new_way, new_count = way, count+dice_number

        while (new_way != 5 and new_count >= len(game_map[new_way])-1):
            if new_way == 0 or new_way == 4:
                new_count = new_count - (len(game_map[new_way])-1)
                new_way = 5
            else:
                new_count = new_count - (len(game_map[new_way])-1)
                new_way = 4

        # 도착 지점을 넘어가는 경우
        if new_way == 5 and new_count >= len(game_map[new_way])-1:
              is_token[way][count] = 0
              current_positions[moving_token] = [-1, -1]
              
              backtracking(cur_round+1, score)
              
              is_token[way][count] = 1
              current_positions[moving_token] = [way, count]
              continue

        current_score = game_map[new_way][new_count]
        
        # 파란색 칸에서 시작하는 경우 경로 변경
        if new_way == 0 and current_score in [10, 20, 30]:
            new_way = current_score // 10
            new_count = 0
        
        # 도착한 칸에 다른 말이 있는지 확인
        if is_token[new_way][new_count]:
            continue
            
        # 말 이동
        is_token[way][count] = 0
        is_token[new_way][new_count] = 1
        current_positions[moving_token] = [new_way, new_count]
        
        backtracking(cur_round+1, score+current_score)
        
        # 말 원위치
        is_token[way][count] = 1
        is_token[new_way][new_count] = 0
        current_positions[moving_token] = [way, count]

backtracking(0, 0)
print(high_score)