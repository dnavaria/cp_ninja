def flipSomeBits(num, arr, n):
	for i in arr:
		num = num ^ (1<<(i-1))
	return num