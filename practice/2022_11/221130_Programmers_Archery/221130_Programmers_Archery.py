def solution(n, info):    
    max_res = [0] * 11
    max_diff = 0
    
    def find_score(i, num_arrow, r_score, a_score, ryan):
        nonlocal max_res, max_diff
        if i == 11:
            if num_arrow > 0:
                ryan[-1] = num_arrow
            if max_diff < r_score-a_score:
                max_diff = r_score-a_score
                max_res = list(ryan)
            elif max_diff == r_score-a_score:
                for j in range(10, -1, -1):
                    if max_res[j] < ryan[j]:
                        max_res = list(ryan)
                        break
                    elif max_res[j] > ryan[j]:
                        break
            return
        
        score = 10-i
        ryan.append(0)
        find_score(i+1, num_arrow, r_score, a_score, ryan)
        ryan.pop()
        if num_arrow > info[i]:
            ryan.append(info[i]+1)
            find_score(i+1, num_arrow-info[i]-1, r_score+score, a_score-score if info[i] > 0 else a_score, ryan)
            ryan.pop()

    a_score = 0
    for i in range(11):
        if info[i] > 0:
            a_score += 10 - i

    find_score(0, n, 0, a_score, [])
    if max_diff <= 0:
        return [-1]

    return max_res