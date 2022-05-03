from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr):
    # two pointer approach of reversing an array
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    return arr

def sol2(arr):
    # pythonic way of reversing an array
    return arr[::-1]

# sol()