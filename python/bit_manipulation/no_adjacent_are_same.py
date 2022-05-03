def checkBits_n(n):
	prev = n & 1
	n>>=1
	while n > 0:
		cur = n & 1
		if prev == cur:
			return False
		n>>=1
		prev = cur
	return True

def allbitset(n):
    return True if ((n+1) & n) == 0 else False

def checkBits(n):
    num = n ^ (n>>1)
    return allbitset(num)

# 1 2 3 => 1 3 6
# 1 5 => sum
# 1 2 3 1 2 3 1 2 3
# 