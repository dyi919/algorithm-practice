import sys

while True:
    num = sys.stdin.readline().strip()

    if num != "0":
        isPalindrome = True

        for i in range(0, len(num)//2+1):
            if num[i] != num[len(num)-1-i]:
                isPalindrome = False
                break

        if isPalindrome:
            print("yes")
        else:
            print("no")
    else:
        break
