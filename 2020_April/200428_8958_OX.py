# gets the total score for an O/X quiz

n = int(input())

for _ in range(n):
    ans = input()
    score = 0
    bonus = 1
    for a in ans:
        if a == "O":
            score += bonus
            bonus += 1
        else: bonus = 1
    print(score)