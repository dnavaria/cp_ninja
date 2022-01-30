
m = 1000000007

def multiplyMatrix(A,B):
    return [[sum(((a)%m*(b)%m)%m for a,b in zip(arow,bcol)) for bcol in zip(*B)] for arow in A]


def fibonacciNumber(n):
    res = [[1,1],[1,1]]
    a = [[1,1],[1,0]]
    while n>0:
        if n&1:
            res = multiplyMatrix(res,a)
        a = multiplyMatrix(a,a)
        n>>=1
    return res[0][0]
        