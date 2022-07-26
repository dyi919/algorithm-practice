# https://www.acmicpc.net/problem/1946

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    candidates = [list(map(int, input().split())) for _ in range(N)]
    candidates.sort(key=lambda x:(x[0], -x[1]))
    count = 0
    highest_interview_rank = 100001

    for _, rank in candidates:
        if rank < highest_interview_rank:
            highest_interview_rank = rank
            count += 1

    print(count)
