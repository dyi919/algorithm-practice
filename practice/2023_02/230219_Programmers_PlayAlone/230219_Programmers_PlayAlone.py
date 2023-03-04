# https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    cards = [0] + cards
    lengths = []
    visited = [False] * (len(cards) + 1)
    visited[0] = True
    
    for card in cards:
        if visited[card]: continue
        
        visited[card] = True
        length = 1
        i = card
        
        while cards[i] != card:
            visited[cards[i]] = True
            i = cards[i]
            length += 1
        
        lengths.append(length)
        
    lengths.sort(reverse=True)
    
    return lengths[0] * lengths[1] if len(lengths) > 1 else 0