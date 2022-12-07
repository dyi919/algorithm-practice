# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    dict = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    
    answer = 0
    mul = 1
    word_len = len(word)
    
    for i in range(1, 6):
        if word_len > 5-i:
            answer += mul * dict[word[5-i]] + 1
        mul = mul * 5 + 1
            
    return answer