# push and pop 1 to n to create a given sequence

seq = []
thru = []
ans = []
n = int(input())
src = [x for x in range(n, 0, -1)]
check = True

for i in range(n): 
    seq.append(int(input()))


seqIdx = 0

while seqIdx < len(seq) and len(ans) <= 2 * len(seq) and check:
    if len(thru) == 0 or thru[len(thru) - 1] < seq[seqIdx]:
        ans.append("+")
        thru.append(src.pop())

    elif thru[len(thru) - 1] == seq[seqIdx]:
        ans.append("-")
        thru.pop()
        seqIdx += 1

    elif thru[len(thru) - 1] > seq[seqIdx]: check = False

if len(ans) != 2 * len(seq):
    print("NO")
else:
    for a in ans: print(a)