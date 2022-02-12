from math import gcd
class Fraction:
	def __init__(self, numerator, denominator) -> None:
		self.numerator = numerator
		self.denominator = denominator

	def add(self, frac):
		if self.denominator == frac.denominator:
			self.numerator += frac.numerator
			return
		else:
			self.numerator = (self.numerator*frac.denominator) + (frac.numerator*self.denominator)
			self.denominator = self.denominator*frac.denominator
			return

	def multiply(self,frac):
		self.numerator *= frac.numerator
		self.denominator *= frac.denominator
	
	def print_frac(self):
		g = gcd(self.numerator,self.denominator)
		print("{0}/{1}".format(self.numerator//g,self.denominator//g))
		
ip1 = [int(i) for i in input().split()]
f1 = Fraction(ip1[0],ip1[1])
t = int(input())
while t > 0:
	ip2 = [int(i) for i in input().split()]
	f2 = Fraction(ip2[1],ip2[2])
	op = ip2[0]
	if op == 1:
		f1.add(f2)
	elif op == 2:
		f1.multiply(f2)
	f1.print_frac()
	t-=1