def rand10(self):
    ret = 40
    while ret >= 40:
        ret = 7 * (rand7() - 1) + (rand7() - 1)
    return ret % 10 + 1
