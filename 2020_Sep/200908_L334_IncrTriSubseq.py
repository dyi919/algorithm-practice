def increasingTriplet(nums):
    mi = float('inf')
    mx = float('inf')

    for n in nums:
        if n <= mi:
            mi = n
        elif n <= mx:
            mx = n
        else:
            return True
    return False


print(increasingTriplet([1, 0, 2, -100, -22, -1]))
