from sys import stdin


def isMixed(notes):
    for i in range(1, len(notes)):
        if abs(notes[i] - notes[i-1]) != 1:
            return True
    return False


notes = [int(i) for i in stdin.readline().split()]

if isMixed(notes):
    print("mixed")
else:
    if notes[0] == 1:
        print("ascending")
    else:
        print("descending")
