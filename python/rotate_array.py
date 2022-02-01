def reverse_array(arr):
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    return arr

def rotate_array(arr,x):
    fh = reverse_array(arr[:x])
    sh = reverse_array(arr[x:])
    fih = fh+sh
    return reverse_array(fih)

n = int(input())
ip = [int(i) for i in input().split()]
x = int(input())
print(rotate_array(ip,x))
