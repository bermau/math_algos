# coding=utf-8
from random import randint
import math

def generate_prime():
	x = randint(100, 9999)
	while True:
		if is_prime(x):
			break
		else:
			x += 1
	return x

def is_prime(x):
	i = 2
	root = math.ceil(math.sqrt(x))
	while i <= root:
		if x % i == 0:
			return False
		i += 1
	return True

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m

if __name__ == "__main__":
	# choose 2 distinct primes
	p = generate_prime()
	while True:
		q = generate_prime()
		if q != p:
			break
	print("p = %d" % p)
	print("q = %d" % q)
	# compute n = pq
	n = p * q
	# compute φ(n)
	n1 = (p - 1) * (q - 1)

	# Choose 1 < e < φ(n), which is coprime to φ(n)
	r = randint(2,100) # For efficiency 2 < e < 100
	while True:
		if gcd(r, n1) == 1:
				break
		else:
			r += 1
	e = r
	print("e = %d" % e)

	# Compute d, the modular multiplicative inverse of e (mod φ(n))
	d = modinv(e, n1)
	print("d = %d" % d)

	m = input("Enter message: ")

	# Encryption of m
	c = (m**e) % n
	print("Encrypted message = %d" % c)

	# Decryption of m
	m1 = (c**d) % n
	print("Decrypted message = %d" % m1)


