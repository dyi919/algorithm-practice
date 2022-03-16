def solution(N, number):
    if N == number: return 1
    cache = {N:1}
    counts = {1:[N]}
    
    for count in range(2, 9):
        counts[count] = []
        
        num = int(str(N) * count)
        if num == number:
            return count
        if num not in cache:
            cache[num] = count
            counts[count].append(num)
        
        for i in range(1, count//2+1):
            for n1 in counts[count-i]:
                for n2 in counts[i]:
                    for newNum in [n1+n2, n1-n2, n2-n1, n1*n2, n1//n2, n2//n1]:
                        if newNum == number:
                            return count
                        if 0 < newNum and newNum not in cache:                    
                            cache[newNum] = count
                            counts[count].append(newNum)
        count += 1
        
    return -1