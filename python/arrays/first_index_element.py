def fidx(ip,x):
    for i in range(len(ip)):
        if ip[i] == x:
            return i
    return -1

n = int(input())
ip = [int(i) for i in input().split()]
x = int(input())
print(fidx(ip,x))

