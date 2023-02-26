# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def validate(s):
    stack = deque()
    
    for c in s:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        
        else:
            if len(stack) == 0: return 0
        
            if c == ']':
                if stack[-1] != '[': return 0

            elif c == '}':
                if stack[-1] != '{': return 0

            elif c == ')':
                if stack[-1] != '(': return 0
            
            stack.pop()
    
    return 1 if len(stack) == 0 else 0

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        answer += validate(rotated)
    
    return answer