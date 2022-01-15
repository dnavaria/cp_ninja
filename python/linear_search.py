from os import read,fstat
from io import BytesIO

def fio():
	return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr, n, x):
	for i in range(0,n):
		if arr[i] == x:
			return i
	return -1

# sol()