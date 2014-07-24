from random import randint
import math

def is_prime(x):
	i = 2
	while i <= math.sqrt(x):
		if x % i == 0:
			return False
		i += 1
	return True

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

def egcd(a, b):
	x, y, u, v = 0, 1, 1, 0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a,x,y,u,v = a,r,u,v,m,n
	return b,x,y

def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m

if __name__ == "__main__":
	p = input("Enter p: ")
	q = input("Enter q: ")
	n = p * q
	n1 = (p - 1) * (q - 1)

	while True:
		r = randint(2,n1)
		if is_prime(r):
			if gcd(r, n1) == 1:
				break

	e = r
	print("e = %d" % e)
	# d = (1 + n1)/e
	d = modinv(e, n1)
	print("d = %d" % d)

	m = input("Enter message: ")
	c = (pow(m, e)) % n
	print("Encrypted message = %d" % c)
	m1 = (pow(c, d)) % n
	print("Decrypted message = %d" % m1)