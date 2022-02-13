
from re import M
from sys import stdin
mod = 10**9+7

def createPref(arr):
    pref = [0]*len(arr)
    ptn = 1
    for i in range(len(arr)):
        pref[i] = ptn
        ptn = (arr[i] * ptn )% mod
    return pref

def createSuff(arr):
    suff = [0]*len(arr)
    ptn = 1
    for i in range(len(arr)-1,-1,-1):
        suff[i] = ptn
        ptn = (ptn * arr[i]) % mod
    return suff


def getProductArrayExceptSelf(arr, n) :
    suff = createSuff(arr)
    pref = createPref(arr)
    
    for i in range(len(arr)):
        arr[i] = (suff[i]*pref[i])%mod
    return arr

def sol2(arr,n):
    ans = [1]*n
    ptn=1
    for i in range(len(arr)):
        ans[i] = ptn
        ptn = (ptn*arr[i])%mod
    ptn = 1
    for i in range(len(arr)-1,-1,-1):
        ans[i] = (ptn*ans[i])%mod
        ptn = (ptn*arr[i])%mod
    return ans
    


def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ") 
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    product = getProductArrayExceptSelf(arr, n)
    printList(product, n)
    
    t -= 1