def lidx(ip,x):
    for i in range(len(ip)-1,0,-1):
        if ip[i] == x:
            return i
    return -1

n = int(input())
ip = [int(i) for i in input().split()]
x = int(input())
print(lidx(ip,x))

