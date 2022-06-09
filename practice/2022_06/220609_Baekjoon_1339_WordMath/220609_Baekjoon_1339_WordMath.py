# 220609_Baekjoon_1339_WordMath

from sys import stdin

ans = 0
N = int(input())
words = []
count_dict = {}
for _ in range(N):
    word = stdin.readline().strip()
    word_length = len(word)
    words.append(word)    
    for c in word:
        word_length -= 1
        if c in count_dict:
            count_dict[c] += 10 ** word_length
        else:
            count_dict[c] = 10 ** word_length
        
count_dict = {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}

multiplier = 9
for v in count_dict.values():
    ans += v * multiplier
    multiplier -= 1

print(ans)