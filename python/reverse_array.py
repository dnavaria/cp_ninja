from os import read,fstat
from io import BytesIO

def fio():
    return BytesIO(read(0,fstat(0).st_size)).readline().decode()

def sol(arr):
    # two pointer approach of reversing an array
    i = 0
    j = len(arr)-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i=i+1
        j=j-1
    return arr

def sol2(arr):
    # pythonic way of reversing an array
    return arr[::-1]

# sol()