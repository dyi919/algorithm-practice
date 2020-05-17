words = []
sub = [[]]
inputFile = open('input.txt', 'r')

n = int(inputFile.readline())

words = inputFile.read().splitlines()

for i in range(len(words) + 1):
    for j in range(i + 1, len(words) + 1):
        sub.append(words[i:j])

inputFile.close()

outputFile = open('output.txt', 'w')
outputFile.write("\n".join(str(item) for item in sub))
outputFile.close()