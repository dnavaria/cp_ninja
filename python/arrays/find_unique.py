from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr):
    ans = arr[0]
    for i in range(1,len(arr)):
        ans ^= arr[i]
    return ans

# sol()