def solution(strings):
    answer = []
    
    for s in strings:
        stack = []
        count = 0
        
        for c in s:
            if c == '0' and len(stack) >= 2 and stack[-1] == stack[-2] == '1':
                stack.pop()
                stack.pop()
                count += 1
                
            else:
                stack.append(c)
        
        pos = -1
        
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '0':
                pos = i
                break

        answer.append(''.join(stack[:pos + 1]) + '110' * count + ''.join(stack[pos + 1:]))

    return answer