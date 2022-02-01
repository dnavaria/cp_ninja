import heapq

def kth(arr,k):
    heapq.nlargest(arr)
    

n = int(input())
k = int(input())
ip = [int(i) for i in input().split()]
print(kth(ip))
