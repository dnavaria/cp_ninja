def findSetBit(N):
    if N and (N & (N-1)):
        cnt = 1
        while N > 0:
            if N & 1:
                return cnt
            cnt+=1
            N>>=1
    return -1