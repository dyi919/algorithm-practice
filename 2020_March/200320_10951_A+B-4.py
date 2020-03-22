# Takes two integers and prints the sum until EOF

import sys

lines = sys.stdin.readlines()

for line in lines:
    a, b = map(int, line.split())
    print(a + b)