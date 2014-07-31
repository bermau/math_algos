from random import randint
import math

def generate_prime():
	x = randint(2, 9999)
	while True:
		print(x)
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
	p = generate_prime()
	while True:
		q = generate_prime()
		if q != p:
			break
	print("p = %d" % p)
	print("q = %d" % q)
	n = p * q
	n1 = (p - 1) * (q - 1)

	while True:
		r = randint(2,n1)
		if is_prime(r):
			if gcd(r, n1) == 1:
				break

	e = r
	print("e = %d" % e)
	d = modinv(e, n1)
	print("d = %d" % d)

	m = input("Enter message: ")
	c = (m**e) % n
	print("Encrypted message = %d" % c)
	m1 = (c**d) % n
	print("Decrypted message = %d" % m1)