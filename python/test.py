from os import read,fstat
from io import BytesIO

def fio():
	return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol():
	pass

str=input().split()
n,m=(int(str[0]),int(str[1]))
li=[[int(j) for j in input().split()] for i in range(n)]
ridx = 0
for i in range(n,0,-1):
	for j in range(0,i):
		print(*li[ridx])
	ridx+=1

