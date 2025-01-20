from itertools import combinations

def solution(dice):
    n = len(dice)
    n_select = n // 2
    max_winning_rate = 0
    answer = []
    
    # 각 주사위의 숫자별 빈도수 계산
    dice_number_counts = []
    for d in dice:
        number_count = {}
        for num in d:
            number_count[num] = number_count.get(num, 0) + 1
        dice_number_counts.append(number_count)
    
    def calculate_score_combinations(dice_indices):
        # 주어진 주사위들의 모든 가능한 합과 그 경우의 수를 계산
        score_counts = {0: 1}  # {합계: 경우의 수}
        
        for dice_idx in dice_indices:
            new_score_counts = {}
            dice_counts = dice_number_counts[dice_idx]
            
            # 현재까지의 각 합계에 대해
            for current_sum, current_count in score_counts.items():
                # 현재 주사위의 각 숫자를 더함
                for number, frequency in dice_counts.items():
                    new_sum = current_sum + number
                    # 새로운 합계의 경우의 수 = 현재까지의 경우의 수 * 현재 숫자의 빈도수
                    new_score_counts[new_sum] = new_score_counts.get(new_sum, 0) + \
                                              current_count * frequency
            
            score_counts = new_score_counts
            
        return score_counts
    
    # 모든 가능한 주사위 조합에 대해
    for comb in combinations(range(n), n_select):
        a_dice = list(comb)
        b_dice = [i for i in range(n) if i not in comb]
        
        # A와 B의 모든 가능한 점수 조합과 경우의 수 계산
        a_scores = calculate_score_combinations(a_dice)
        b_scores = calculate_score_combinations(b_dice)
        
        # 승리 횟수 계산
        win_count = 0
        total_cases = 0
        
        # 각 가능한 점수 조합에 대해 승패 판정
        for a_sum, a_count in a_scores.items():
            for b_sum, b_count in b_scores.items():
                case_count = a_count * b_count
                if a_sum > b_sum:  # A의 승리
                    win_count += case_count
                total_cases += case_count
        
        # 승률 계산 및 최대 승률 갱신
        winning_rate = win_count / total_cases
        if winning_rate > max_winning_rate:
            max_winning_rate = winning_rate
            answer = [i + 1 for i in a_dice]
    
    return answer