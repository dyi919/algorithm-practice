# prints self numbers < 10000

def SelfNum():
    a = []

    for i in range(1, 10001):
        if i in a:
            n = i + sum([int(x) for x in list(str(i))])
            a.append(n)
        else:
            print(i)
            n = i + sum([int(x) for x in list(str(i))])
            a.append(n)

SelfNum()