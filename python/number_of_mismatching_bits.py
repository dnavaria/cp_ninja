def numberOfMismatchingBits(first, second):
    cnt = 0
    xor = first ^ second
    while xor:
        xor = xor & (xor-1)
        cnt+=1
    return cnt


print(numberOfMismatchingBits(6,20))