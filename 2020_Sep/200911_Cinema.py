def maxNumberOfFamilies(n, reservedSeats):
    from collections import defaultdict
    d, res = defaultdict(set), 0
    for r, c in reservedSeats:
        d[r].add(c)
    for k, v in d.items():
        if 4 not in v and 5 not in v and 6 not in v and 7 not in v:
            if 2 not in v and 3 not in v and 8 not in v and 9 not in v:
                res += 2
            else:
                res += 1
        elif 6 not in v and 7 not in v and 8 not in v and 9 not in v:
            res += 1
        elif 2 not in v and 3 not in v and 4 not in v and 5 not in v:
            res += 1
    res += 2 * (n - len(d.keys()))
    return res


seats = [[4, 3], [1, 4], [4, 6], [1, 7]]
print(maxNumberOfFamilies(4, seats))
