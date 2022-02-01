import sys
def kths(arr,k):
    s = 0
    mn = -1
    c=0
    while s <len(arr):
        if arr[s] > mn:
            mn = arr[s]
            c+=1
        if c == k:
            return arr[s]
        s+=1
    return -1

def kthl(arr,k):
    e = len(arr)-1
    mn = sys.maxsize
    c=0
    while e >=0:
        if arr[e] < mn:
            mn = arr[e]
            c+=1
        if c == k:
            return arr[e]
        e-=1
    return -1


def kthSmallestLargest(arr,k):
    arr.sort()
    large = kthl(arr,k)
    small = kths(arr,k)
    
    return small,large
    

n = int(input())
k = int(input())
ip = [int(i) for i in input().split()]
print(kth(ip))
