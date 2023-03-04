# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    
    for number in numbers:
        temp = number
        i = 0
        
        while temp > 0:
            temp, mod = divmod(temp, 2)
            if mod == 0: break
            i += 1
        
        if i == 0:
            answer.append(number + 1)
        else:
            answer.append(number + 2 ** i - 2 ** (i - 1))
        
    return answer